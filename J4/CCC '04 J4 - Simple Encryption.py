# Canadian Computing Competition: 2004 Stage 1, Junior #4
# https://dmoj.ca/problem/ccc04j4

import sys

change = sys.stdin.readlines(1)[0].strip()
word = sys.stdin.readlines(1)[0].strip()
cycle = 0
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
text = ""

for character in word:
    if character in alphabet:
        if cycle == len(change):
            cycle = 0
        text += alphabet[(alphabet.find(character) + alphabet.find(change[cycle]))%26]
        cycle += 1
print(text)
