#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list is not None:
        remove_double(my_list)
        return (sum_list(my_list))
    

def remove_double(my_list):
    unique_list = []
    
    for el in my_list:
        if el not in unique_list:
            unique_list.append(el)
    
    my_list.clear()
    my_list.extend(unique_list)

def sum_list(my_l):
    sum_item = 0
    for i in my_l:
        sum_item += i
    return (sum_item)
