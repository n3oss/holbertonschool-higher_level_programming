#!/usr/bin/python3
import sys
a = sys.argv
if __name__ == "__main__":
    b = 0
    for x in range(1, len(a)):
        c = int(a[x])
        b = b + c
    print(b)
