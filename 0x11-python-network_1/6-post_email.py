#!/usr/bin/python3
"""Send POST request to URL with email as parameter"""

import requests
import sys

if len(sys.argv) != 3:
    print("Usage: python script.py <URL> <email>")
    sys.exit(1)

url = sys.argv[1]
email = sys.argv[2]

data = {"email": email}

try:
    response = requests.post(url, data=data)
    response.raise_for_status()

    response_body = response.text
    print(response_body)
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
