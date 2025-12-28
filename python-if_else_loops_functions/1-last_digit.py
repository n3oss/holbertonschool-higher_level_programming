#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
a = abs(number) % 10
if number < 0:
    a = -a
if a > 5:
    h = "and is greater than 5"
elif a < 6 and a != 0:
    h = "and is less than 6 and not 0"
else:
    h = "and is 0"
print(f"Last digit of {number} is {a} {h}")
