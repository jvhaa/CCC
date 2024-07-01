import sys
import math

data = sys.stdin.readlines(1)[0].strip().split(" ")

day = int(data[0])
month = int(data[1])

space = 0

l = 0

print("Sun Mon Tue Wed Thr Fri Sat")

s = ""
for i in range(day - 1):
    space += 1 * 4

for i in range(7 - (day - 1)):
    l += 1
    s += "   " + str(l)

print("  " +  " "* space + s.strip())

for k in range(math.ceil((month + (day-1)) / 7) - 1):
    s = ""
    l += 1
    space = 1 * (3-len(str(l)))
    s += str(l)
    for i in range(6):
        if (l + 1) <= month:
            l += 1
        else:
            break
        s += " " * (4 - len(str(l)))
        s += str(l)
    print(" "* space + s.strip())
