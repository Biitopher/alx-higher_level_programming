#!/usr/bin/python3
"""Script taking URL to send request to URL displaying variable value"""

import requests
import sys

if len(sys.argv) != 2:
    print("Usage: python script.py <URL>")
    sys.exit(1)

url = sys.argv[1]

try:
    response = requests.get(url)
    response.raise_for_status()

    x_request_id = response.headers.get("X-Request-Id")

    if x_request_id:
        print(x_request_id)
    else:
        print("X-Request-Id not found in response headers.")
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
