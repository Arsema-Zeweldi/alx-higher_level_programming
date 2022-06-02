#!/usr/bin/python3
def add(argv):
    a = len(argv) - 1
    if a == 0:
        print("{:d}".format(a))
        return
    else:
        b = 1
        c = 0
        while b <= a:
            c += int(argv[b])
            b += 1
        print("{:d}".format(c))


if __name__ == "__main__":
    import sys
    add(sys.argv)
