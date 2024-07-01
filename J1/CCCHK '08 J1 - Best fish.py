# Canadian Computing Competition: 2008HK Stage 1, Junior #1
# https://dmoj.ca/problem/hkccc08j1

import sys

Casper = int(sys.stdin.readlines(1)[0])
c = 0
for i in range(Casper):
    fish = sys.stdin.readlines(1)[0].split(" ")
    f = int(fish[0]) * int(fish[1])
    if f > c:
        c = f

Natalie = int(sys.stdin.readlines(1)[0])
n = 0
for i in range(Natalie):
    fish = sys.stdin.readlines(1)[0].split(" ")
    f = int(fish[0]) * int(fish[1])
    if f > n:
        n = f

if n > c:
    print("Natalie")
elif c > n:
    print("Casper")
else:
    print("Tie")
