# Canadian Computing Competition: 2012 Stage 1, Junior #1
# https://dmoj.ca/problem/ccc12j1

import sys

limit = int(sys.stdin.readlines(1)[0])
speed = int(sys.stdin.readlines(1)[0])

total = speed - limit

if total > 0 and total < 21:
    print("You are speeding and your fine is $100.")
elif total > 20 and total < 31:
    print("You are speeding and your fine is $270.")
elif total > 30:
    print("You are speeding and your fine is $500.")
else:
    print("Congratulations, you are within the speed limit!")
