import sys, heapq
input = sys.stdin.readline
N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    A, B, C = map(int, input().split())
    graph[A].append((B, C))
    graph[B].append((A, C))

INF = int(1e9)
d = [INF] * (N+1)
before_node = [0] * (N+1)
q = []
d[1] = 0
heapq.heappush(q,(1, 0))

while q:
    now, now_d = heapq.heappop(q)
    if d[now] < now_d:
        continue
    for edge in graph[now]:
        next_n, cost = edge
        if d[next_n] > now_d + cost:
            d[next_n] = now_d + cost
            before_node[next_n] = now
            heapq.heappush(q,(next_n, d[next_n]))

print(N-1)
for i in range(2, N+1):
    print(i, before_node[i])