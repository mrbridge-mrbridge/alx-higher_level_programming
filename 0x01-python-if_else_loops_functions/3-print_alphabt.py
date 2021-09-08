#!/usr/bin/python3
for alph in range(97, 123):
    if (alph == 101) or (alph == 113):
        continue
    else:
        print('{:c}'.format(alph), end='')
