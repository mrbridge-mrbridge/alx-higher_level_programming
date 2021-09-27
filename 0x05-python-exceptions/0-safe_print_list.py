#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    if x > 0:
        for i in range(x - 1):
            print(my_list[i], end='')
        print('')

try:
    safe_print_list()
except:
    print('Exception found')
