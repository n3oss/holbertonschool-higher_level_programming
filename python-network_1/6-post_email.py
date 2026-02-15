#!/usr/bin/python3
"""python post request with  an email parameter"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    payload = {"email": email}
    r = requests.post(url, data=payload)
    print(r.text)
