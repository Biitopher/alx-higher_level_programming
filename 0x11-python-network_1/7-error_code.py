#!/usr/bin/python3
"""Displays the body of the response requested to the URL"""

import requests
import sys

if len(sys.argv) != 2:
    print("Usage: python script.py <URL>")
    sys.exit(1)

url = sys.argv[1]

try:
    response = requests.get(url)
    response.raise_for_status()

    response_body = response.text
    print(response_body)

    if response.status_code >= 400:
        print(f"Error code: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
