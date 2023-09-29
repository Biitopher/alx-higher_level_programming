#!/usr/bin/python3
"""Takes URL and sends request to URL to display body of response"""

import urllib.request
import sys
import urllib.error

if len(sys.argv) != 2:
    print("Usage: python script.py <URL>")
    sys.exit(1)

url = sys.argv[1]

try:
    with urllib.request.urlopen(url) as response:
        response_body = response.read().decode("utf-8")
        print(response_body)
except urllib.error.HTTPError as e:
    print(f"Error code: {e.code}")
except Exception as e:
    print(f"Error: {e}")
