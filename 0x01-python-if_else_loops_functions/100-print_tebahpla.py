#!/usr/bin/python3
for alph in range(122, 96, -1):
    if alph % 2 != 0:
        alph = alph - 32
    print('{}'.format(chr(alph)), end='')
