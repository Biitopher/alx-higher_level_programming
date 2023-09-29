#!/usr/bin/python3
"""GitHub credentials using GitHub API for display"""

import requests
import sys

if len(sys.argv) != 3:
    print("Usage: python script.py <username> <personal_access_token>")
    sys.exit(1)

username = sys.argv[1]
access_token = sys.argv[2]

url = "https://api.github.com/user"
headers = {
    "Authorization": f"Basic {username}:{access_token}",
}

try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()

    data = response.json()
    user_id = data.get("id")

    if user_id:
        print(f"Your GitHub user ID is: {user_id}")
    else:
        print("User ID not found in the response.")
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
