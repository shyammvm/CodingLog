# Coding log with auto revision reminder

This repo keeps track of all the daily practise coding questions pushed into this repo using Notion and reminds you to revise them regularly.

### Stats
![LeetCode Stats](https://leetcard.jacoblin.cool/shyammvm?theme=dark&font=Karma&ext=heatmap)


### Features

- Store every solved problem as a **Markdown file** in this repo
- Automatically extract:
  - Problem name
  - Problem link
  - Difficulty
  - Topic (from folder structure)
  - Last solved date (from git commit history)
  - Next revision date (auto-calculated by difficulty)
  - GitHub link to code
- Syncs entries to a Notion database via GitHub Actions
- Updates Notion only when a problem’s file changes

### Setup:
1. Fork this repo :  [Gthub Repo](git@github.com:shyammvm/CodingPractiseAutoRevisionReminder.git)
2. Save the [Notion page template](https://automatic-alpaca-193.notion.site/Coding-Log-Template-265e48f402248097b944da66533c300d?source=copy_link)
3. Create the Notion Integration token
    1.	Go to https://www.notion.com/my-integrations.
    2. Click + New Integration.
    3. Fill out
       1. Name → e.g., LeetCode Sync.
       2. Associated workspace → choose the workspace where your Problems database lives (the template you saved).
       3. Capabilities → Read, Insert and Update
       4. Click Submit.
       5. Copy the Internal Integration Token → this is what you put into your GitHub secret NOTION_TOKEN.
4.  Share your Notion Database with the Integration
    1.  Open the database you created from the template
    2.  Click Share (top-right)
    3.  Invite the integration you just made (e.g., LeetCode Sync)
    4.  Without this step, the integration cannot read/write your database
5. Get your Notion Database ID
	1.	Open the database as a full page in Notion
	2.	Copy the URL — it looks like:
        ```
        https://www.notion.so/username/Your-Database-Name-263e48f4022480ee8de6d41f26db1b74
        ```
    3.	The long string at the end is your Database ID:
        ```
        263e48f4022480ee8de6d41f26db1b74
        ```
    4. Save this as NOTION_DATABASE_ID in Github Secrets
 6. Now whenever you are pushing a solution to this repo, use the following template
       1. Create an .md file with the following template:
    ```
        # Problem: $PROBLEM_NAME

        # Link: [Insert LeetCode Link]  
        # Difficulty: $DIFFICULTY  

        ---

        ## Solution

        \`\`\`python
        # Your code here
        \`\`\`

        ---

        ## Notes
        - Approach:
        - Time Complexity:
        - Space Complexity:
    ```
    2. You can automate this by using VSCode snippets:
         1. Press `Cmd+Shift+P` (Mac) / `Ctrl+Shift+P` (Windows/Linux) to open the Command Palette.
         2. Type `Preferences: Configure User Snippets` and select it.
         3. Choose `New Global Snippets file` (or select your workspace if you want it local eg:.md).
         4. Give it a name, e.g., `lcproblem`.
         5. Inside the JSON file, add the above template
         6. Save the snippet file.
         7. Now in any Markdown file, type lcproblem and press Tab → your full problem template will be inserted automatically.
    2. Or you can run the leetcode.sh file in the repository (Instructions in the file)
 7. Now pushing this .md file into your repo will automatically create the entries in Notion.
 8. Revision will be shown in the 'Revision Log' view and on the 'Calender View'. You can also add this to your Notion Calender to be reminded on your calender feed.
