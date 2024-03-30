#!/usr/bin/python3
"""A script that takes GitHub credentials (username and personal access token)
and uses the GitHub API to display the user's id.
"""
import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    # Prepare the authentication header
    auth = (username, password)

    # Make the request to the GitHub API
    response = requests.get('https://api.github.com/user', auth=auth)

    # Check if the request was successful and print the user id
    if response.status_code == 200:
        user_data = response.json()
        print(user_data['id'])
    else:
        print(None)

