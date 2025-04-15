from collections import deque
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
edges = [[] for _ in range(N+1)]
degree = [0] * (N+1)

for _ in range(M):
    orders = list(map(int, input().split()))
    for i in range(2, orders[0]+1):
        degree[orders[i]] += 1
        edges[orders[i-1]].append(orders[i])

q = deque([])
result = []
for i in range(1, N+1):
    if degree[i] == 0:
        q.append(i)

while q:
    now = q.popleft()
    result.append(now)
    for n in edges[now]:
        degree[n] -= 1
        if degree[n] == 0:
            q.append(n)

if len(result) != N:
    print(0)
else:
    for n in result:
        print(n)