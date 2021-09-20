#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tp, tuple_y, tuple_x = (), (), ()
    for i in range(2):
        if tuple_a[i] == ():
            tuple_x[i] = 0
        else:
            tuple_x[i] = tuple_a[i]

        if tuple_b[i] == ():
            tuple_y[i] = 0
        else:
            tuple_y[i] = tuple_a[i]
        tp[i] = tuple_x[i] + tuple_y[i]
    return tp
