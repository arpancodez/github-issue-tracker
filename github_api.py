import requests
from config import GITHUB_TOKEN

BASE_URL = "https://api.github.com"

def get_issues(owner, repo, state="open"):
    url = f"{BASE_URL}/repos/{owner}/{repo}/issues"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    params = {"state": state}
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    return response.json()

def comment_issue(owner, repo, issue_number, comment):
    url = f"{BASE_URL}/repos/{owner}/{repo}/issues/{issue_number}/comments"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    response = requests.post(url, headers=headers, json={"body": comment})
    response.raise_for_status()
    return response.json()
