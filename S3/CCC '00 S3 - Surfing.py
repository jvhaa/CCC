# Canadian Computing Competition: 2000 Stage 1, Junior #5, Senior #3
# https://dmoj.ca/problem/ccc00s3

from collections import deque
import sys
input = sys.stdin.readline

websites = {}

def bfs(start, end):
  queue = deque([start])
  visited = set()
  while queue:
    node = queue.popleft()
    if node not in visited:
      visited.add(node)
      if node == end:
        return True
      for child in websites[node]:
        if child not in visited:
          queue.append(child)
  return False

for i in range(int(input())):
  url = input().strip()
  websites[url] = []
  while True:
    start  = -1
    line = input().strip()
    if "A HREF" in line:
      for loops in range(line.count("A HREF")):
        start = line.find('<A HREF="', start+1)
        end = line.find('">', start)
        link = line[start+9:end]
        websites[url].append(link)
    if line == "</HTML>":
      break

for key, value in websites.items():
  for v in value:
    print(f"Link from {key} to {v}")

while True:
  start = input().strip()
  if start == "The End":
    break
  end = input().strip()
  if bfs(start, end):
    print(f"Can surf from {start} to {end}.")
  else:
    print(f"Can't surf from {start} to {end}.")
