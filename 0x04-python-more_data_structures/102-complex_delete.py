#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if a_dictionary:
        keys_remove = list()

        for k, v in a_dictionary.items():
            if (v == value):
                keys_remove.append(k)

        for k in keys_remove:
            del a_dictionary[k]

    return (a_dictionary)
