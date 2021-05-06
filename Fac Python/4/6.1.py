from itertools import count, cycle
from sys import argv

path, *args, end = argv
try:
    print(args)
    end = int(end)
except ValueError:
    print('You mast enter integer positive numbers')
    exit()
counter = 1
for elem in cycle(args):
    if counter <= end:
        print(elem)
        counter += 1
    else:
        break
