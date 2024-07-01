# Canadian Computing Competition: 2009 Stage 1, Junior #1
# https://dmoj.ca/problem/ccc09j1

import sys
import math

number = int(sys.stdin.readlines(1)[0])

if number < 6:
    i = 1 + math.floor((number)/2)
else:
    i = math.floor((number)/2) - (number-6)

print(i)
