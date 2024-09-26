from sys import stdin
from collections import deque
n, m = map(int, stdin.readline().split())
graph = []
goal = []

result = [[]]

for i in range(n):
    g = list(map(int, stdin.readline().split()))
    for j in range(m):
        if g[j] == 2:
            goal.append(i)
            goal.append(j)
    graph.append(g)

visited = [[False for _ in range(m)] for i in range(n)]
def dfs():
    q = deque([])
    
    q.append()
    visited.append()
