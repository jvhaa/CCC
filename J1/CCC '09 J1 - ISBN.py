# Canadian Computing Competition: 2009 Stage 1, Junior #1
# https://dmoj.ca/problem/ccc09j1

import sys

f = int(sys.stdin.readlines(1)[0])
s = int(sys.stdin.readlines(1)[0])
t = int(sys.stdin.readlines(1)[0])

print("The 1-3-sum is ", str(f*1+s*3+t*1 + 91), sep = "")
