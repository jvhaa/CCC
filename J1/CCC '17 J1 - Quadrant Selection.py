# Canadian Computing Competition: 2017 Stage 1, Junior #1
# https://dmoj.ca/problem/ccc17j1

import sys

x = int(sys.stdin.readlines(1)[0])
y = int(sys.stdin.readlines(1)[0])

if x > 0 and y > 0:
    print(1)
elif y > 0:
    print(2)
elif x > 0:
    print(4)
else:
    print(3)
