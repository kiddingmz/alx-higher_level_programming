#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    aux = []

    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            aux.append(True)
        else:
            aux.append(False)
    return (aux)
