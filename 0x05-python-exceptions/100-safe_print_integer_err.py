#!/usr/bin/python3
import sys
def safe_print_integer_err(value):
    try:
        print('{:d}'.format(value))
        return True
    except TypeError as f:
        sys.stderr.write('Exception:', f)
        return False
