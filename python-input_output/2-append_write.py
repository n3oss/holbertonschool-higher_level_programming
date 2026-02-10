#!/usr/bin/python3
"""Python file append"""


def append_write(filename="", text=""):
    """appends file"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
