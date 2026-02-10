#!/usr/bin/python3
"""Python class and inheritance"""


class MyList(list):
    """list sorting"""
    def print_sorted(self):
        print(sorted(self))
