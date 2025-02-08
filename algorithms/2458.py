import sys, heapq
input = sys.stdin.readline
N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)

INF = int(1e9)
d = [[INF]*(N+1) for _ in range(N+1)]

def dijkstra(n):
    q = []
    d[n][n] = 0
    heapq.heappush(q, (0, n))
    while q:
        now = heapq.heappop(q)
        if d[n][now[1]] < now[0]:
            continue
        for e in graph[now[1]]:
            if d[n][e] > now[0] + 1:
                d[n][e] = now[0] + 1
                heapq.heappush(q, (d[n][e], e))

for i in range(1, N+1):
    dijkstra(i)

result = 0
for i in range(1, N+1):
    tmp = True
    for j in range(1, N+1):
        if d[i][j] == INF and d[j][i] == INF:
            tmp = False
            break
    if tmp:
        result += 1

print(result)