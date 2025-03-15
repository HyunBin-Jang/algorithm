import sys, heapq
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
degree = [0] * (N+1)
q = []

for _ in range(M):
    A, B = map(int, input().split())
    degree[B] += 1
    graph[A].append(B)

for i in range(1, N+1):
    if degree[i] == 0:
        heapq.heappush(q, i)

result = []
while q:
    now = heapq.heappop(q)
    for i in graph[now]:
        degree[i] -= 1
        if degree[i] == 0:
            heapq.heappush(q, i)
    result.append(now)

for n in result:
    print(n,"",end="")
