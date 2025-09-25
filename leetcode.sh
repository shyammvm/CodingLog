#!/bin/bash

# Mac:
# make this file executable with: chmod +x leetcode.sh if running for the first time.
# Usage: ./leetcode.sh <domain> <problem-name> <difficulty>
# Example: ./leetcode.sh arrays two_sum Easy

# Windows:
# Usage: bash new_problem.sh <domain> <problem-name> <difficulty>
# Example: bash new_problem.sh arrays two_sum Easy

DOMAIN=$1
PROBLEM_NAME=$2
DIFFICULTY=$3
FOLDER="./$DOMAIN"
FILE="Problems/$FOLDER/$PROBLEM_NAME.md"

# Create domain folder if it doesn't exist
mkdir -p "Problems/$FOLDER"

# Create the markdown file with template
cat > "$FILE" <<EOL
# Problem: $PROBLEM_NAME

# Link: [Insert LeetCode Link]  
# Difficulty: $DIFFICULTY  

---

## Solution
## 1. Approach 1
\`\`\`python
# Your code here
\`\`\`

---

#### Notes
- Approach:
- Time Complexity:
- Space Complexity:
EOL

echo "✅ Created $FILE"