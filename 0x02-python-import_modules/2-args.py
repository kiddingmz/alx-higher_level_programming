#!/usr/bin/python3
import sys as system

argv = system.argv
length = len(argv)

print("{:d} arguments:".format(length - 1))

for arg in range(1, length):
    print("{:d}: {:s}".format(arg, argv[arg]))
