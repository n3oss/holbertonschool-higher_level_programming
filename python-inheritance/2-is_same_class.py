#!/usr/bin/python3
"""Return object that makes sure its int float etc"""


def is_same_class(obj, a_class):
    """get elements and make sure theyre int ,float"""

    if isinstance(obj, a_class):
        return type(obj) is a_class
    return False
