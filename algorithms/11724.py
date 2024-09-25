from collections import deque
from sys import stdin

N,M = map(int, stdin.readline().split())

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (N + 1)

def bfs(start):
    q = deque([])
    q.append(start)
    visited[start] = True
    while q:
        t = q.popleft()
        for n in graph[t]:
            if not visited[n]:
                q.append(n)
                visited[n] = True
    return 1

result = 0
for i in range(1, N + 1):
    if not visited[i]:
        result += bfs(i)

print(result)