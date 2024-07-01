# Canadian Computing Competition: 2004 Stage 1, Junior #1
# https://dmoj.ca/problem/ccc04j1

import sys

area = int(sys.stdin.readlines(1)[0])

side = 0

for i in range(1, area+1):
    if area / i >= i:
        side += 1
    else:
        break
    
print("The largest square has side length " + str(side) + ".")
