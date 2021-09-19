#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if len(my_list) <= idx < 0:
        return my_list

    copy = my_list
    copy[idx] = element
    return copy
