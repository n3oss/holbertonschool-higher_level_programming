#!/usr/bin/python3
"""python"""


def write_file(filename="", text=""):
    """python"""
    with open(filename, "w", encoding="utf-8")as f:
        return f.write(text)
