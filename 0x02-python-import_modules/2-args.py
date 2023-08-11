#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    length = len(sys.argv)

    print("{} {}".format(
        (length - 1),
        "arguments." if length == 1 else "arguments:"
    ))

    length = 0
    for arg in sys.argv:
        if length != 0:
            print("{}: {}".format(length, arg))
        length += 1
