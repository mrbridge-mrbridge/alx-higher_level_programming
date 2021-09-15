#!/usr/bin/python3
if __name__ == '__main__':
   from sys import argv

   count = len(argv) 
    if count = 1:
        print('{} argument:'.format(count))
    elif count = 0:
        print('{} arguments.'.format(count))
    else:
        print('{} arguments:'.format(count))

    if count >= 1:
        for i in range(1, count+1, 1):
            print('{}: {}'.format(i, argv[i]))

