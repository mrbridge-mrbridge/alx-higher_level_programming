#!/usr/bin/python3
def best_score(a_dictionary):
    big = 0
    for k in a_dictionary:
        if a_dictionary[k] > big:
            big = a_dictionary[k]
    if len(a_dictionary) == 0:
        return None
    else:
        return (k for k in a_dictionary if a_dictionary[k] == big)
