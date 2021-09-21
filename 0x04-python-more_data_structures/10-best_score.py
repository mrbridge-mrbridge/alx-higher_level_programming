#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary or len(a_dictionary) == 0:
        return None
    big = 0
    for k, v in a_dictionary.items():
        if v > big:
            big = v
    for k, v in a_dictionary.items():
        if big == v:
            return k
