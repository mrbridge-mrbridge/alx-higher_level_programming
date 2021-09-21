#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list
    for i in range(len(new_list) - 1):
        for elm[i] in new_list:
            if elm[i] == search:
                new_list.insert(i, search)
    return new_list
