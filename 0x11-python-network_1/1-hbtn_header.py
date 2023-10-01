#!/usr/bin/python3
"""Sends request to URL and displays value of ID"""

import urllib.request
import sys

if len(sys.argv) != 2:
    print("Usage: python script.py <URL>")
    sys.exit(1)

url = sys.argv[1]

try:
    with urllib.request.urlopen(url) as response:
        x_request_id = response.getheader("X-Request-Id")
        if x_request_id:
            print(x_request_id)
        else:
            print()
except Exception as e:
    print(f"Error: {e}")
