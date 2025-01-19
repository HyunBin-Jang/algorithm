import heapq, sys
input = sys.stdin.readline
V, E = map(int, input().split())
K = int(input())
INF = 10**9
distance = [INF] * (V + 1)
graph = [[] for i in range(V + 1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v,w))

q = []
heapq.heappush(q, (0, K))
distance[K] = 0
while q:
    now = heapq.heappop(q)
    if distance[now[1]] < now[0]:
        continue
    for e in graph[now[1]]:
        if now[0] + e[1] < distance[e[0]]:
            distance[e[0]] = now[0] + e[1]
            heapq.heappush(q, (distance[e[0]], e[0]))

for i in range(1, V + 1):
    if distance [i] == INF:
        print("INF")
    else:
        print(distance[i])