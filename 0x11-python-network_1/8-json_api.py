#!/usr/bin/python3
"""Script taking in letter and sends POST request"""

import requests
import sys

if len(sys.argv) == 2:
    letter = sys.argv[1]
else:
    letter = ""

url = "http://0.0.0.0:5000/search_user"
params = {"q": letter}

try:
    response = requests.post(url, data=params)
    response.raise_for_status()

    try:
        data = response.json()
        if data:
            print(f"[{data['id']}] {data['name']}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
