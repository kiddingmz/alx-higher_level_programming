#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    j = 0
    for i in my_list:
        try:
            if (j == x):
                break
            print("{}".format(i), end="")
            j += 1
        except IndexError:
            break
    print()
    return (j)
