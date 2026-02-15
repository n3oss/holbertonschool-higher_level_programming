#!/usr/bin/python3
"""python post request with  an email parameter"""
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    data = {
            "email": email
    }

    encoded = urllib.parse.urlencode(data).encode("utf-8")

    request = urllib.request.Request(url, data=encoded, method="POST")

    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))
