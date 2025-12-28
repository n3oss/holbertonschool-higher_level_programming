#!/usr/bin/python3
def print_last_digit(number):
    numberq = abs(number)
    a = numberq % 10
    print(a, end="")
    return a
