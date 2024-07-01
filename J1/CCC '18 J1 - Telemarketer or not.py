# Canadian Computing Competition: 2018 Stage 1, Junior #1
# https://dmoj.ca/problem/ccc18j1

import sys

data1 = int(sys.stdin.readlines(1)[0])
data2 = int(sys.stdin.readlines(1)[0])
data3 = int(sys.stdin.readlines(1)[0])
data4 = int(sys.stdin.readlines(1)[0])


if (data1 == 8 or data1 == 9) and (data2 == data3) and (data4 == 8 or data4 == 9):
    print("ignore")
else:
    print("answer")
