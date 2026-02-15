#!/usr/bin/python3
"""python requests fetching data"""
import requests


r = requests.get('https://intranet.hbtn.io/status')

print("Body response:")
print("\t- type: {}".format(type(r.text)))
print("\t- content: {}".format(r.text))
