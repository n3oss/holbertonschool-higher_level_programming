#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    a = a_dictionary.copy()
    for x in a:
        a[x] = a[x] * 2
    return a
