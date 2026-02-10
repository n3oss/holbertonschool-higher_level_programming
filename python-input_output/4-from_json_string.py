#!/usr/bin/python3
"""
Module for JSON string conversion
"""
import json


def from_json_string(my_str):
    """Returns the JSON representation of an object (string)"""
    return json.loads(my_str)
