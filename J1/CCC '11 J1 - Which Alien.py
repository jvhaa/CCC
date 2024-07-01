# Canadian Computing Competition: 2011 Stage 1, Junior #1
# https://dmoj.ca/problem/ccc11j1

import sys

a = int(sys.stdin.readlines(1)[0])
e = int(sys.stdin.readlines(1)[0])

if a > 2 and e < 5:
    print("TroyMartian")
if a < 7 and e > 1:
    print("VladSaturnian")
if a < 3 and e < 4:
  print("GraemeMercurian")
