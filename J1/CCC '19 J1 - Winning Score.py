# Canadian Computing Competition: 2019 Stage 1, Junior #1
# https://dmoj.ca/problem/ccc19j1

import sys

def score():
    score = 0
    for i in range(3):
        sa = int(sys.stdin.readlines(1)[0])
        score += sa * (3-i)
    return score
    
a = score()
b = score()

if a > b:
    print("A")
elif a < b:
    print("B")
else:
    print("T")
