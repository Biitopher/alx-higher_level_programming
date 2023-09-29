#!/usr/bin/python3
"""Sending POST request using URL"""

import urllib.request
import urllib.parse
import sys

if len(sys.argv) != 3:
    print("Usage: python script.py <URL> <email>")
    sys.exit(1)

url = sys.argv[1]
email = sys.argv[2]

data = {"email": email}
data = urllib.parse.urlencode(data).encode("utf-8")

try:
    with urllib.request.urlopen(url, data=data) as response:
        response_body = response.read().decode("utf-8")
        print(response_body)
except Exception as e:
    print(f"Error: {e}")
