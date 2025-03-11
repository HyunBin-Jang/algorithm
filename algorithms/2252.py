from collections import deque
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
degree = [0] * (N+1)
graph = [[] for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    degree[B] += 1

q = deque([])
for i in range(1, N+1):
    if degree[i] == 0:
        q.append(i)

result = []
while q:
    now = q.popleft()
    for i in graph[now]:
        degree[i] -= 1
        if degree[i] == 0:
            q.append(i)
    result.append(now)

for r in result:
    print(r,"",end="")