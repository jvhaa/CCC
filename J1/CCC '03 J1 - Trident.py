# Canadian Computing Competition: 2003 Stage 1, Junior #1
# https://dmoj.ca/problem/ccc03j1

import sys 

top = int(sys.stdin.readlines(1)[0])
mid = int(sys.stdin.readlines(1)[0])
bot = int(sys.stdin.readlines(1)[0])

for i in range(top):
    print("*", " "*mid, "*", " "*mid, "*", sep ="")
    
print("*"* (3 + 2*mid))

for i in range(bot):
    print(" "* (1+mid), "*", sep ="")
