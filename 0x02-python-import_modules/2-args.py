#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    length = len(sys.argv)
    txt = "arguments." if length == 1 else "arguments:" 
    print("{:d} {:s}".format(length - 1, txt))

    for arg in range(1, length):
        print("{:d}: {:s}".format(arg, sys.argv[arg]))
