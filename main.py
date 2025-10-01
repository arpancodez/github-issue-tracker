import argparse
from github_api import get_issues, comment_issue
from summarizer import summarize_text

def main():
    parser = argparse.ArgumentParser(description="GitHub Issue Tracker CLI")
    parser.add_argument("owner", help="GitHub repo owner (e.g., torvalds)")
    parser.add_argument("repo", help="GitHub repo name (e.g., linux)")
    args = parser.parse_args()

    print(f"\n🔍 Fetching issues for {args.owner}/{args.repo}...\n")
    issues = get_issues(args.owner, args.repo)

    for issue in issues:
        title = issue.get("title", "")
        body = issue.get("body", "")
        number = issue.get("number")
        url = issue.get("html_url")

        summary = summarize_text(body)

        print(f"#{number} | {title}")
        print(f"Summary: {summary}")
        print(f"Link: {url}\n{'-'*60}\n")

if __name__ == "__main__":
    main()
