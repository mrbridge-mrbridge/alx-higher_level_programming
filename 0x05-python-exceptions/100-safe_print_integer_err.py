#!/usr/bin/python3
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError) as f:
        import sys
        print("Exception: {}".format(f), file = sys.stderr)
        return False
