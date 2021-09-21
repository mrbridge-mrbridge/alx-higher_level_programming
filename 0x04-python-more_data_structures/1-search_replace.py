#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list
    for elm in new_list:
        if elm is search:
            elm = replace
    return new_list

