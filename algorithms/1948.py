from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
degree = [0] * (n+1)

for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c, i))
    degree[b] += 1
start, end = map(int, input().split())

d = [0] * (n+1)
q = deque([])
q.append((start, 0))
path = [[] for _ in range(n+1)]

while q:
    now = q.popleft()
    for edge in graph[now[0]]:
        degree[edge[0]] -= 1
        if d[edge[0]] < d[now[0]] + edge[1]:
            d[edge[0]] = d[now[0]] + edge[1]
            path[edge[0]] = list(set(path[now[0]] + [edge[2]]))
        elif d[edge[0]] == d[now[0]] + edge[1]:
            path[edge[0]] = list(set(path[edge[0]] + path[now[0]] + [edge[2]]))
        if degree[edge[0]] == 0:
            q.append((edge[0], now[1] + 1))
print(d[end])
print(len(set(path[end])))
