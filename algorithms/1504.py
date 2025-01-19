import sys, heapq

input = sys.stdin.readline
N, E = map(int, input().split())

INF = 10 ** 9
graph = [[] for i in range(N+1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v,w))
    graph[v].append((u,w))

v1, v2 = map(int, input().split())

def dijkstra(start, end):
    distance = [INF] * (N + 1)
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    while q:
        now = heapq.heappop(q)
        if now[1] == end:
            break
        if now[0] > distance[now[1]]:
            continue
        for e in graph[now[1]]:
            if e[1] + now[0] < distance[e[0]]:
                distance[e[0]] = e[1] + now[0]
                heapq.heappush(q, (distance[e[0]], e[0]))
    return distance[end]
if v1 == 1 and v2 == N:
    result = dijkstra(1, N)
else:
    result = min(dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, N),
             dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, N))

if result >= INF:
    print(-1)
else:
    print(result)