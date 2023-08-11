#!/usr/bin/python3
if __name__ == "__main__":
    import sys as system

    argv = system.argv
    length = len(argv)
    txt = "arguments." if length == 1 else "argumentes:" 
    print("{:d} {txt}".format(length - 1, txt=txt))

    for arg in range(1, length):
        print("{:d}: {:s}".format(arg, argv[arg]))
