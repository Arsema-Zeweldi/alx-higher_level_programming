#!/usr/bin/python3
def print_last_digit(number):
    a = int(repr(number)[-1])
    print("{}".format(a), end='')
    return a
