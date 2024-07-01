# Canadian Computing Competition in HK: 2015 Stage 1, Junior #1
# https://dmoj.ca/problem/hkccc15j1

import sys

count = int(sys.stdin.readlines(1)[0])
try1 = sys.stdin.readlines(1)[0].strip().split(" ")
try2 = sys.stdin.readlines(1)[0].strip().split(" ")
one = 0
two = 0

for i in range(count):
    if try2[i] == "rock" and try1[i] == "paper":
        one += 1
    elif try2[i] == "paper" and try1[i] == "scissors":
        one += 1
    elif try2[i] == "scissors" and try1[i] == "rock":
        one += 1
    elif try1[i] == "rock" and try2[i] == "paper":
        two += 1
    elif try1[i] == "paper" and try2[i] == "scissors":
        two += 1
    elif try1[i] == "scissors" and try2[i] == "rock":
        two += 1

print(str(one) + " " + str(two))
