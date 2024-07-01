# Canadian Computing Competition: 2021 Stage 1, Junior #1
# https://dmoj.ca/problem/ccc21j1

import sys
boil = int(sys.stdin.readlines(1)[0])
p = 5 * boil - 400
print(p)
if p > 100:
    print(-1)
elif p == 100:
    print(0)
else:
    print(1)
