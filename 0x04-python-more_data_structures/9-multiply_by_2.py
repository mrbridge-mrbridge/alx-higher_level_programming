#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    m = {}
    for k, v in a_dictionary.items():
        m = {k: v*2}
    return m
