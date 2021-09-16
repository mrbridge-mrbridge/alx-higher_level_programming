#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv, exit
    count = len(argv) - 1
    operator = int(argv[2])
    if count != 3:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)
    else:
        if operator == '+':
            print('{} {} {} = {}'.format(int(argv[1]), operator, int(argv[3]), add(int(argv[1]), int(argv[3]))))
        elif operator == '-':
             print('{} {} {} = {}'.format(int(argv[1]), operator, int(argv[3]), sub(int(argv[1]), int(argv[3]))))
        elif operator == '*':
             print('{} {} {} = {}'.format(int(argv[1]), operator, int(argv[3]), mul(int(argv[1]), int(argv[3]))))
        elif operator == '/':
             print('{} {} {} = {}'.format(int(argv[1]), operator, int(argv[3]), div(int(argv[1]), int(argv[3]))))
        else:
            print('Unknown operator. Available operators: +, -, * and /')
            exit(1)
