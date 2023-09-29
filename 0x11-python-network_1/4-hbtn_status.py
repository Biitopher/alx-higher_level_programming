#!/usr/bin/python3
"""Script that fetchs status"""

import requests

url = "https://alx-intranet.hbtn.io/status"

try:
    response = requests.get(url)
    response.raise_for_status()

    content = response.text

    print("Body response:")
    print(f"\t- type: {type(content)}")
    print(f"\t- content: {content}")
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
