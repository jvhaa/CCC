# Canadian Computing Competition: 2016 Stage 1, Junior #1
# https://dmoj.ca/problem/ccc16j1

import sys

wins = 0
for line in sys.stdin:
    if line.strip() == "W":
        wins += 1
        
if wins < 1:
    print(-1)
elif wins < 3: 
    print(3)
elif wins < 5:
    print(2)
elif wins < 7 and wins > 4:
    print(1)

wins = 0
