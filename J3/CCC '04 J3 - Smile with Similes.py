# Canadian Computing Competition: 2004 Stage 1, Junior #3
# https://dmoj.ca/problem/ccc04j3

import sys

s = int(sys.stdin.readlines(1)[0])
e = int(sys.stdin.readlines(1)[0])

s_list = []
e_list = []

for i in range(s):
    s_list.append(sys.stdin.readlines(1)[0].strip())

for i in range(e):
    e_list.append(sys.stdin.readlines(1)[0].strip())
    
for i in range(s):
    for l in range(e):
        print(s_list[i], "as", e_list[l], sep=' ')
