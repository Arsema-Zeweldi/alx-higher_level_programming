#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    n = 0
    for c in range(x):
        value = my_list[c]
        try:
            print("{:d}".format(value), end='')
            n += 1
        except Exception:
            continue
    print("")
    return n
