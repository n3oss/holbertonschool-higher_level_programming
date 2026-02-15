#!/usr/bin/python3
"""script that displays the value of the variavble"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    r = requests.get(url)
    request_id = r.headers.get('X-Request-Id')

    if request_id:
        print(request_id)
