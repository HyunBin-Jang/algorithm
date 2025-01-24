import sys, heapq
input = sys.stdin.readline
N, M, X = map(int, input().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    start, end, cost = map(int, input().split())
    graph[start].append((end, cost))


INF = int(1e9)

def dijkstra(start, end):
    d = [INF] * (N + 1)
    d[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    while q:
        now = heapq.heappop(q)
        if d[now[1]] < now[0]:
            continue
        if now[1] == end:
            return d[now[1]]
        for e in graph[now[1]]:
            if d[e[0]] > e[1] + now[0]:
                d[e[0]] = e[1] + now[0]
                heapq.heappush(q, (d[e[0]], e[0]))
    return d[end]


d_come = [INF] * (N + 1)
d_come[X] = 0
q = []
heapq.heappush(q, (0, X))

while q:
    now = heapq.heappop(q)
    if d_come[now[1]] < now[0]:
        continue
    for e in graph[now[1]]:
        if d_come[e[0]] > e[1] + now[0]:
            d_come[e[0]] = e[1] + now[0]
            heapq.heappush(q, (d_come[e[0]], e[0]))

d_go = [INF] * (N+1)
for i in range(1, N+1):
    d_go[i] = dijkstra(i, X)

result = []
for i in range(1, N+1):
    result.append(d_go[i] + d_come[i])

print(max(result))