# Canadian Computing Competition: 2007 Stage 1, Junior #1
# https://dmoj.ca/problem/ccc07j1

import sys

i1 = int(sys.stdin.readline())
i2 = int(sys.stdin.readline())
i3 = int(sys.stdin.readline())

greatest = max(i1, i2)
greatest = max(greatest, i3)

smallest = min(i1, i2)
smallest = min(smallest, i3)

if i1 != smallest and i1 != greatest:
    print (i1)

if i2 != smallest and i2 != greatest:
    print (i2)

if i3 != smallest and i3 != greatest:
    print (i3)
