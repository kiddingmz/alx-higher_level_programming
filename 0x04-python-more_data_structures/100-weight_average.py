#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is not None:
        num, sc = 0, 0

        for val in my_list:
            num += val[0] * val[1]
            sc += val[1]
        return (num / sc)

    return (0)
