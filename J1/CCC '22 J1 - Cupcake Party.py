# Canadian Computing Competition: 2022 Stage 1, Junior #1
# https://dmoj.ca/problem/ccc22j1

import sys

medium = int(sys.stdin.readlines(1)[0]) * 8 
small = int(sys.stdin.readlines(1)[0]) * 3 

print(medium + small - 28)
