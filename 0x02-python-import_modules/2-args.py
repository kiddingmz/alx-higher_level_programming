#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    length = len(sys.argv)
    txt = "arguments." if length == 1 else "arguments:" 
    print("{:d} {txt}".format(length - 1, txt=txt))

    for arg in range(1, length):
        print("{:d}: {}".format(arg, sys.argv[arg]))
