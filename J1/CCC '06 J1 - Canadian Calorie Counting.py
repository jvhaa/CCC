# Canadian Computing Competition: 2005 Stage 1, Junior #1
# https://dmoj.ca/problem/ccc05j1

import sys

calorie = 0

for i in range(4):
    option = int(sys.stdin.readlines(1)[0])
    if i == 0:
        if option == 1:
            calorie += 461
        elif option == 2:
            calorie += 431
        elif option == 3:
            calorie += 420
    elif i == 2:
        if option == 1:
            calorie += 130
        elif option == 2:
            calorie += 160
        elif option == 3:
            calorie += 118
    elif i == 1:
        if option == 1:
            calorie += 100
        elif option == 2:
            calorie += 57
        elif option == 3:
            calorie += 70
    else:
        if option == 1:
            calorie += 167
        elif option == 2:
            calorie += 266
        elif option == 3:
            calorie += 75
        
print("Your total Calorie count is " + str(calorie) + ".")
