#!/usr/bin/python3
"""Fetches a URL and displays the X-Request-Id header value"""
import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]

    with urllib.request.urlopen(url) as response:
        request_id = response.headers.get("X-Request-Id")

    print(request_id)
