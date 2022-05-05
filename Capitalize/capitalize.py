# first and last names of people begin with a capital letter in their passports.
# For example, alison heck should be capitalised correctly as Alison Heck.


import math
import os
import random
import re
import sys


def solve(s):
    words = s.split(" ")
    print(words)
    capitalized_words = []
    for w in words:
        if len(w) > 0 and ord(w[0]) >= 97 and ord(w[0]) <= 122:
            w = chr(ord(w[0])-32) + w[1:]
        capitalized_words.append(w)

    return " ".join(capitalized_words)


if __name__ == '__main__':

    s = input()

    result = solve(s)

    print(result)
