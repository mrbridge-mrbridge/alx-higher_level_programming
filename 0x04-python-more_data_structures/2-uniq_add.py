#!/usr/bin/python3
def uniq_add(my_list=[]):
    total = 0
    n = set(my_list[:])
    for elm in n:
        total += elm
    return total
