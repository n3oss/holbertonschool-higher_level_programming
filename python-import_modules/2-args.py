#!/usr/bin/python3
import sys
if __name__ == "__main__":
    a = sys.argv
    argc = len(a) - 1
    if argc == 0:
        print("0 arguments.")
    elif argc == 1:
        print("1 argument:")
        print("1: {}".format(a[1]))
    else:
        print("{} arguments:".format(argc))
        for i in range(1, len(a)):
            print("{}: {}".format(i, a[i]))
