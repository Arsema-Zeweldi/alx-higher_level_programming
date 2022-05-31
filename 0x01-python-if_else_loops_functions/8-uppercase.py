#!/usr/bin/python3
def uppercase(str):
    d = list(str)
    for c in range(len(d)):
        if (ord(d[c]) > 96 and ord(d[c]) < 123):
            d[c] = chr(ord(d[c]) - 32)
    print("{:s}".format("".join(d)))
