import heapq
N, M = map(int,input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    A, B, C = map(int,input().split())
    graph[A].append([B, C])
    graph[B].append([A, C])
INF = 10**9
d = [INF] * (N + 1)
visited = [False] * (N + 1)

d[1] = 0
q = []
heapq.heappush(q, [d[1], 1])

while q:
    t = heapq.heappop(q)
    if not visited[t[1]]:
        visited[t[1]] = True
        for g in graph[t[1]]:
            if not visited[g[0]]:
                d[g[0]] = min(d[g[0]], d[t[1]] + g[1])
                heapq.heappush(q, [d[g[0]], g[0]])

print(d[N])