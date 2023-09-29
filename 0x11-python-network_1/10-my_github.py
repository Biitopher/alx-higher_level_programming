#!/usr/bin/python3
"""GitHub credentials using GitHub API for display"""

import requests
import sys

username = sys.argv[1]
access_token = sys.argv[2]

headers = {
    "Authorization": f"Basic {username}:{access_token}"
}

url = "https://api.github.com/user"
response = requests.get(url, headers=headers)

if response.status_code == 200:
    user_data = response.json()
    user_id = user_data["id"]
    print(f"Your GitHub user ID is: {user_id}")
elif response.status_code == 401:
    print("Authentication failed. Please check your username and access token.")
else:
    print(f"An error occurred. Status code: {response.status_code}")
