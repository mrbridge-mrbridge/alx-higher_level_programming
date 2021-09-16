#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    count = len(argv) - 1
    add = 0
    for i in range(1, count + 1, 1):
        add = add + int(argv[i])
    print(add)
