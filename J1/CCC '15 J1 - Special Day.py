# Canadian Computing Competition: 2015 Stage 1, Junior #1
# https://dmoj.ca/problem/ccc15j1

import sys

month = int(sys.stdin.readlines(1)[0])
day = int(sys.stdin.readlines(1)[0])

if month == 2 and day == 18:
    print("Special")
elif month > 2 or (month == 2 and day > 18):
    print("After")
else:
    print("Before")
