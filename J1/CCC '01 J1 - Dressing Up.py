# Canadian Computing Competition: 2001 Stage 1, Junior #1
# https://dmoj.ca/problem/ccc01j1

h = int(input())
spaces = 2 * h - 2
stars = 1

for i in range(1, h + 1):
    for j in range(1, stars + 1):
        print("*", end="")
    for j in range(1, spaces + 1):
        print(" ", end="")
    for j in range(1, stars + 1):
        print("*", end="")

    if i <= h // 2:
        spaces -= 4
        stars += 2
    else:
        spaces += 4
        stars -= 2
    
    print("")
