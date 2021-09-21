#!/usr/bin/python3
__import__('functools').reduce
def uniq_add(my_list=[]):
    n = set(my_list[:])
    return (reduce(lambda x, y: x + y, n))

