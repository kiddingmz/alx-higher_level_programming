#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    length = len(sys.argv)

    print("{:d} {:s}".format(
        (length - 1),
        "arguments." if length == 1 else (
            "argument:" if length == 2 else "arguments:"
            )
    ))

    for arg in range(1, length):
        print("{:d}: {:s}".format(arg, sys.argv[arg]))
