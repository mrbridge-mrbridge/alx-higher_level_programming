#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list
    for elm in new_list:
        if elm == search:
            elm = replace
    return new_list

