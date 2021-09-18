#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv
    count = len(argv) - 1
    
    if count != 3:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        sys.exit(1)
    
    a = int(argv[1])
    b = int(argv[3])
    op = ['+', '-', '*', '/']

    if argv[2] not in op:
        print('Unknown operator. Available operators: +, -, * and /')
        sys.exit(1)
    elif argv[2] == '+':
        print('{} {} {} = {}'.format(a, argv[2], b, add(a, b)))
    elif argv[2] == '-':
        print('{} {} {} = {}'.format(a, argv[2], b, sub(a, b)))
    elif argv[2] == '*':
        print('{} {} {} = {}'.format(a, argv[2], b, mul(a, b)))
    elif argv[2] == '/':
        print('{} {} {} = {}'.format(a, argv[2], b, div(a, b)))
