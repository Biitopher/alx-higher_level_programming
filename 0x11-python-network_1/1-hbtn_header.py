#!/usr/bin/python3
"""Sends request to URL and displays value of ID"""

import urllib.request
import sys

if __name__ == "__main__":
    """Request to the URL and displays value of variable"""
    with urllib.request.urlopen(argv[1]) as response:
        x_request_id = response.info().get('X-Request-Id')
        print(x_request_id)
