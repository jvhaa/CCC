# Canadian Computing Competition: 2023 Stage 1, Junior #1
# https://dmoj.ca/problem/ccc23j1

import sys

recieved = int(sys.stdin.readlines(1)[0])
destroyed = int(sys.stdin.readlines(1)[0])

points = 0

if recieved > destroyed:
    points += 500
print(points + recieved * 50 - destroyed * 10)
