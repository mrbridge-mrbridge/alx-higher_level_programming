#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = my_list[:]
    for i in range(len(new) - 1):
        if new[i] == search:
            new[i] = replace
    return new
