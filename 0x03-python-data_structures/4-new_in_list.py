#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if my_list:
        copy = my_list[:]
        if 0 > idx >= len(my_list):
            return my_list
        else:
            copy[idx] = element
            return copy
