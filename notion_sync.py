import os
import re
import requests
import subprocess

NOTION_TOKEN = os.getenv("NOTION_TOKEN")
DATABASE_ID = os.getenv("NOTION_DATABASE_ID")

headers = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}

def get_commit_date():
    result = subprocess.run(
        ["git", "log", "-1", "--format=%aI"],
        capture_output=True, text=True
    )
    return result.stdout.strip()

def get_git_link(filepath):
    repo_url = subprocess.run(
        ["git", "config", "--get", "remote.origin.url"],
        capture_output=True, text=True
    ).stdout.strip()
    repo_url = repo_url.replace("git@github.com:", "https://github.com/").replace(".git", "")
    branch = subprocess.run(["git", "rev-parse", "--abbrev-ref", "HEAD"], capture_output=True, text=True).stdout.strip()
    return f"{repo_url}/blob/{branch}/{filepath}"

def parse_metadata(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    problem = re.search(r"Problem:\s*(.+)", content)
    link = re.search(r"Link:\s*(.+)", content)
    diff = re.search(r"Difficulty:\s*(.+)", content)
    return {
        "problem": problem.group(1).strip() if problem else os.path.basename(filepath),
        "link": link.group(1).strip() if link else "",
        "difficulty": diff.group(1).strip().capitalize() if diff else "Medium"
    }

def send_to_notion(problem, link, difficulty, date, git_link):
    url = "https://api.notion.com/v1/pages"
    data = {
        "parent": {"database_id": DATABASE_ID},
        "properties": {
            "Problem Name": {"title": [{"text": {"content": problem}}]},
            "Problem Link": {"url": link if link else None},
            "Difficulty": {"select": {"name": difficulty}},
            "Last Solved": {"date": {"start": date}},
            "Git Link": {"url": git_link}
        }
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code != 200:
        print("❌ Error:", response.text)
    else:
        print(f"✅ Added {problem} to Notion")

if __name__ == "__main__":
    changed_files = subprocess.run(
        ["git", "diff", "--name-only", "HEAD~1", "HEAD"],
        capture_output=True, text=True
    ).stdout.splitlines()

    commit_date = get_commit_date()

    for file in changed_files:
        if file.endswith(".md"):
            meta = parse_metadata(file)
            git_link = get_git_link(file)
            send_to_notion(meta["problem"], meta["link"], meta["difficulty"], commit_date, git_link)