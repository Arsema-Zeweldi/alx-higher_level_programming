#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    counter = 0
    for n in range(x):
        try:
            print(my_list[n], end='')
            counter += 1
        except Exception as err:
            break
        print('')
        return counter
