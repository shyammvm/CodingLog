import os

def generate_problem_list(base_dir="Problems"):
    problem_list = []
    for topic in sorted(os.listdir(base_dir)):
        topic_path = os.path.join(base_dir, topic)
        if os.path.isdir(topic_path):
            problem_list.append(f"## {topic}\n")
            for problem in sorted(os.listdir(topic_path)):
                if problem.endswith(".md"):
                    problem_name = os.path.splitext(problem)[0]
                    problem_list.append(f"- [{problem_name}]({base_dir}/{topic}/{problem})")
            problem_list.append("")  # newline
    return "\n".join(problem_list)

def update_readme(readme_path="README.md", base_dir="Problems"):
    # Read the existing README
    with open(readme_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    
    # Keep the first 9 lines intact
    header = "".join(lines[:6]) if len(lines) >= 9 else "".join(lines)
    
    # Generate problem list
    problem_list = generate_problem_list(base_dir)
    
    # Write back updated README
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(header)
        f.write("\n")
        f.write(problem_list)

if __name__ == "__main__":
    update_readme()