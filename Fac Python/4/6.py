from itertools import count, cycle
from sys import argv

path, start, end = argv
try:
    start = int(start)
    end = int(end)
except ValueError:
    print('You mast enter integer positive numbers')
    exit()


if end > start:
    for i in count(start):
        if i <= end:
            print(i)

        else:
            break
else:
    print('End must be grate than start')
