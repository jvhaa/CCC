# Canadian Computing Competition: 2020 Stage 1, Junior #1
# https://dmoj.ca/problem/ccc20j1

import sys
small = int(sys.stdin.readlines(1)[0])
medium = int(sys.stdin.readlines(1)[0])
large = int(sys.stdin.readlines(1)[0])

if small + medium * 2 + large * 3 >= 10:
    print("happy")
else:
    print("sad")
