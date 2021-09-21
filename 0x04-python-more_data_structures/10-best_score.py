#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary or len(a_dictionary) == 0:
        return None
    big = 0
    for k in a_dictionary:
        if a_dictionary[k] > big:
            big = a_dictionary[k]
            ret = k
        return (ret)
