#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = o
    for i in range(x):
        try:
            print("{:d}".format(my_list[i] if int(my_list[i]) else continue), end="")
            count += 1
        except (IndexError, TypeError):
            break
    return count
