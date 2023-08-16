#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if a_dictionary is not None:
        aux_d = sorted(a_dictionary.items())

        for item in aux_d:
            k, v = item
            print("{0}: {1}".format(k,v))
