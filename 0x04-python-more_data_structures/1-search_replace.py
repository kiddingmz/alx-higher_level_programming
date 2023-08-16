#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    if my_list is not None:
        for v in my_list:
            if v == search:
                new_list.append(replace)
            else:
                new_list.append(v)
        return (new_list)
    return (my_list)
