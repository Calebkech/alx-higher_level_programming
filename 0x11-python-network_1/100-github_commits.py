#!/usr/bin/python3
"""A script that lists 10 commits (from the most recent to oldest)
of the repository “rails” by the user “rails” using the GitHub API.
"""
import requests
import sys

if __name__ == "__main__":
    repository = sys.argv[1]
    owner = sys.argv[2]

    url = f"https://api.github.com/repos/{owner}/{repository}/commits"
    response = requests.get(url)

    if response.status_code == 200:
        commits = response.json()[:10]  # Get the first 10 commits
        for commit in commits:
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print(f"{sha}: {author_name}")
    else:
        print("Error:", response.status_code)

