#!/usr/bin/python3
def safe_function(fct, *args):
    try:
        res = fct(*args)
        return res
    except Exception as ex:
        print('Exception: {}'.format(ex), file=sys.sterr)
        return None
