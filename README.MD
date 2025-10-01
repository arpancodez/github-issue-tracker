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
```text
github_issue_tracker/
│── main.py              # Entry point (CLI interface)
│── config.py            # Handles API tokens & config
│── github_api.py        # GitHub API interactions
│── summarizer.py        # NLP summarization logic
│── cache.py             # (Optional) caching with SQLite/TinyDB
│── utils.py             # Helper functions & formatting
│── requirements.txt     # Dependencies
