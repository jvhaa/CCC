# Canadian Computing Competition: 2005 Stage 1, Junior #1
# https://dmoj.ca/problem/ccc05j1

import sys

a = int(sys.stdin.readlines(1)[0])
b = int(sys.stdin.readlines(1)[0])
c = int(sys.stdin.readlines(1)[0])

A = max(a - 100, 0) * 0.25 + 0.15 * b + 0.2 * c
B = max(a - 250, 0) * 0.45 + 0.35 * b + 0.25 * c

print("Plan A costs %.2f" % A)
print("Plan B costs %.2f" % B)

if A < B:
    print("Plan A is cheapest.")
elif A > B:
    print("Plan B is cheapest.")
else:
    print("Plan A and B are the same price.")
