#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv, exit
    count = len(argv) - 1
    operator = count[2]
    if count != 3:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)
    else:
        if operator == '+':
            print('{} {} {} = {}'.format(int(argv[1]), operator, int(argv[3]), add))
        elif operator == '-':
             print('{} {} {} = {}'.format(int(argv[1]), operator, int(argv[3]), sub))
        elif operator == '*':
             print('{} {} {} = {}'.format(int(argv[1]), operator, int(argv[3]), mul))
        elif operator == '/':
             print('{} {} {} = {}'.format(int(argv[1]), operator, int(argv[3]), div))
        else:
            print('Unknown operator. Available operators: +, -, * and /')
            exit(1)
