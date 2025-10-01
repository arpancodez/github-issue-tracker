import os

# Load GitHub personal access token from environment variable
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

if not GITHUB_TOKEN:
    raise ValueError("⚠️ Please set GITHUB_TOKEN as environment variable!")
