# 📌 GitHub Issue Tracker with AI Summarizer

A **command-line tool** written in Python that fetches issues from any GitHub repository and provides **AI-powered summaries** of issue descriptions using NLP.  
This helps developers **quickly scan issues** without reading through long texts.  

---

## ✨ Features
- 🔍 Fetch issues from any GitHub repository.  
- 📝 Summarize issue descriptions using **Hugging Face Transformers**.  
- 🎨 Clean command-line interface (optional: colorized output with `rich`).  
- 💬 Post comments on issues directly from the CLI.  
- 📦 Optional caching using SQLite/TinyDB.  

---

## 📂 Project Structure
github_issue_tracker/
│── main.py # Entry point (CLI interface)
│── config.py # Handles API tokens & config
│── github_api.py # GitHub API interactions
│── summarizer.py # NLP summarization logic
│── cache.py # (Optional) caching with SQLite/TinyDB
│── utils.py # Helper functions & formatting
│── requirements.txt # Dependencies


---

## ⚡ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/github-issue-tracker.git
   cd github-issue-tracker


Set up a virtual environment (recommended)
python -m venv venv
source venv/bin/activate   # (Linux/Mac)
venv\Scripts\activate      # (Windows)

Install dependencies
pip install -r requirements.txt

🔑 GitHub Authentication
You need a GitHub Personal Access Token to authenticate.
Go to GitHub → Developer Settings → Tokens
Generate a new token with repo scope.
Export it as an environment variable:

export GITHUB_TOKEN="your_personal_token"   # Linux/Mac
set GITHUB_TOKEN="your_personal_token"      # Windows

🚀 Usage
Fetch and summarize issues for a repo:
python main.py <owner> <repo>
Example:
python main.py octocat hello-world

✅ Example Output:
🔍 Fetching issues for octocat/hello-world...

#12 | Fix README formatting
Summary: Updates documentation for better readability.
Link: https://github.com/octocat/hello-world/issues/12
------------------------------------------------------------
#13 | Add API endpoint for comments
Summary: Implements a new API endpoint to fetch and create comments.
Link: https://github.com/octocat/hello-world/issues/13
------------------------------------------------------------

🛠 Tech Stack

Python 3.8+
Requests
 – GitHub API communication
Transformers
 – NLP summarization
Torch
 – Required backend for models
Rich
 – (Optional) pretty CLI output

📌 Future Improvements
✅ Add --ai-label flag to auto-suggest issue labels.
✅ Export summaries as Markdown/HTML reports.
✅ Add interactive mode with Textual TUI.

🤝 Contributing
Pull requests are welcome! Please open an issue first to discuss any major changes.
