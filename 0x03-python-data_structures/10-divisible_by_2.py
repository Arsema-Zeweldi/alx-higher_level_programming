#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if not my_list:
        return
    for n in my_list:
        if n % 2 == 0:
            return n
