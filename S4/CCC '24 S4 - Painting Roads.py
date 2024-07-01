# Canadian Computing Competition: 2024 Stage 1, Senior #4
# https://dmoj.ca/problem/ccc24s4

import sys
from collections import defaultdict

sys.setrecursionlimit(3000000)

nodes, edges = map(int, input().split())
graph = defaultdict(list)

for i in range(edges):
    a, b = map(int, input().split())
    graph[a].append((b, i))
    graph[b].append((a, i))

visited = set()
answer = ["G"] * edges

def dfs(node, state):
    for neigh, index in graph[node]:
        if neigh in visited:
            continue
        visited.add(neigh)
        if state == 0:
            answer[index] = "B"
        else:
            answer[index] = "R"
        dfs(neigh, state^1)

for i in range(1, nodes+1):
    if i not in visited:
        visited.add(i)
        dfs(i, 0)

print("".join(answer))
