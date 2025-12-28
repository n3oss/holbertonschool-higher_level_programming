#!/usr/bin/python3
def uppercase(str):
    b = ""
    for x in str:
        if ord('a') <= ord(x) <= ord('z'):
            b += chr(ord(x) - 32)
        else:
            b += x
    print("{}".format(b))
