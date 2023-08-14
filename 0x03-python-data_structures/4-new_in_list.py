#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    tmp_list = my_list.copy()
    if (idx < 0) or (idx > (len(tmp_list) - 1)):
        return (tmp_list)
    tmp_list[idx] = element
    return (tmp_list)

