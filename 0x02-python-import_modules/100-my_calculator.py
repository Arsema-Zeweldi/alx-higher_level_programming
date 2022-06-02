#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv
    operator = list(r'+-*/')

    if len(argv) != 4:
        print("Usage: {} <a> <operator> <b>".format(argv[0]))
        exit(1)

    a = int(argv[1])
    b = int(argv[3])

    if argv[2] not in operator:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        if argv[2] == '+':
            print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
        elif argv[2] == '-':
            print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
        elif argv[2] == '*':
            print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
        else:
            print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
