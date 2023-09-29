#!/usr/bin/python3
"""GitHub credentials using GitHub API for display"""

import requests
from sys import argv

if __name__ == "__main__":
    """Uses GItHub API to display credentials"""
    username = argv[1]
    password = argv[2]
    url = 'https://api.github.com/user'
    r = requests.get(url, auth=(username, password))
    try:
        print(r.json().get('id'))
    except:
        pass
