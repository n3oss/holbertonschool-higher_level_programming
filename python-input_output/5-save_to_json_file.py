#!/usr/bin/python3
"""Python json"""
import json


def save_to_json_file(my_obj, filename):
    """python doc"""
    with open(filename, "w", encoding="utf-8") as f:
        return json.dump(my_obj, f)
