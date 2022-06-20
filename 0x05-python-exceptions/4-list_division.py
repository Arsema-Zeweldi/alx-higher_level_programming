#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for c in range(list_length):
        n = 0
        try:
            a, b = (my_list_1[c], my_list_2[c])
            n = a / b
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            new_list.append(n)
    return new_list
