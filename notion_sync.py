import os
import re
import requests
import subprocess
import glob
import logging

# ----------------- CONFIG -----------------
NOTION_TOKEN = os.getenv("NOTION_TOKEN")
DATABASE_ID = os.getenv("NOTION_DATABASE_ID")

HEADERS = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}

# ----------------- LOGGING -----------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

# ----------------- HELPERS -----------------
def get_git_link(filepath):
    """Generate GitHub file link"""
    repo_url = subprocess.run(
        ["git", "config", "--get", "remote.origin.url"],
        capture_output=True, text=True
    ).stdout.strip()
    repo_url = repo_url.replace("git@github.com:", "https://github.com/").replace(".git", "")
    branch = subprocess.run(
        ["git", "rev-parse", "--abbrev-ref", "HEAD"], 
        capture_output=True, text=True
    ).stdout.strip()
    return f"{repo_url}/blob/{branch}/{filepath}"

def get_commit_date():
    """Get latest commit date in ISO format"""
    result = subprocess.run(
        ["git", "log", "-1", "--format=%aI"],
        capture_output=True, text=True
    )
    return result.stdout.strip()

def parse_metadata(filepath):
    """Extract Problem, Link, Difficulty from markdown"""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    problem = re.search(r"^\s*#?\s*Problem:\s*(.+)", content, re.MULTILINE)
    link = re.search(r"^\s*#?\s*Link:\s*(.+)", content, re.MULTILINE)
    diff = re.search(r"^\s*#?\s*Difficulty:\s*(.+)", content, re.MULTILINE)

    return {
        "problem": problem.group(1).strip() if problem else os.path.basename(filepath),
        "link": link.group(1).strip() if link else "",
        "difficulty": diff.group(1).strip().capitalize() if diff else "Medium"
    }

def page_exists(problem_name):
    """Check if a page with this Problem already exists"""
    url = f"https://api.notion.com/v1/databases/{DATABASE_ID}/query"
    payload = {
        "filter": {
            "property": "Problem",
            "title": {
                "equals": problem_name
            }
        }
    }
    response = requests.post(url, headers=HEADERS, json=payload)
    if response.status_code != 200:
        logging.error(f"Failed to query Notion for {problem_name}: {response.text}")
        return False
    results = response.json().get("results", [])
    return len(results) > 0

def send_to_notion(problem, link, difficulty, date, git_link):
    """Create a new page in Notion"""
    url = "https://api.notion.com/v1/pages"
    data = {
        "parent": {"database_id": DATABASE_ID},
        "properties": {
            "Problem": {"title": [{"text": {"content": problem}}]},
            "Problem Link": {"url": link if link else None},
            "Difficulty": {"select": {"name": difficulty}},
            "Last Solved": {"date": {"start": date}},
            "Git Link": {"url": git_link}
        }
    }
    response = requests.post(url, headers=HEADERS, json=data)
    if response.status_code != 200:
        logging.error(f"Failed to add {problem}: {response.text}")
    else:
        logging.info(f"✅ Added {problem} to Notion")

# ----------------- MAIN -----------------
if __name__ == "__main__":
    logging.info("Starting Notion sync...")
    commit_date = get_commit_date()
    all_files = glob.glob("Problems/**/*.md", recursive=True)
    logging.info(f"Found {len(all_files)} markdown files in Problems folder.")

    for file in all_files:
        meta = parse_metadata(file)
        git_link = get_git_link(file)

        if not page_exists(meta["problem"]):
            logging.info(f"Adding new problem: {meta['problem']}")
            send_to_notion(meta["problem"], meta["link"], meta["difficulty"], commit_date, git_link)
        else:
            logging.warning(f"{meta['problem']} already exists in Notion, skipping.")

    logging.info("Notion sync completed.")