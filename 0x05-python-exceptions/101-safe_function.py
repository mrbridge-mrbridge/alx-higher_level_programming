#!/usr/bin/python3
def safe_function(fct, *args):
    try:
        res = fct(*args)
        return res
    except Exception as ex:
        import sys
        print('Exception: {}'.format(ex), file=sys.stderr)
        return None
