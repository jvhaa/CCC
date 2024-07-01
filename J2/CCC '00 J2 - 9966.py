# Canadian Computing Competition: 2000 Stage 1, Junior #2
# https://dmoj.ca/problem/ccc00j2

import sys

n = int(sys.stdin.readlines(1)[0])
x = int(sys.stdin.readlines(1)[0])
total = 0

same = ["1", "0", "8"]

for i in range(n, x+1):
    text = str(i)[::-1]
    subtext = ""
    for l in range(len(text)):
        if text[l] == "6":
            subtext += "9"
        elif text[l] == "9":
            subtext += "6"
        elif text[l] in same:
            subtext += text[l]

    if subtext == str(i):
        total += 1

print(total)
