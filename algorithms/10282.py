import sys, heapq
input = sys.stdin.readline
T = int(input())

INF = int(1e9)
for _ in range(T):
    n, d, c = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    distance = [INF] * (n+1)
    for _ in range(d):
        a, b, s = map(int, input().split())
        graph[b].append((a,s))

    q = []
    heapq.heappush(q, (0, c))
    distance[c] = 0
    while q:
        now = heapq.heappop(q)
        if distance[now[1]] < now[0]:
            continue
        for g in graph[now[1]]:
            if distance[g[0]] > g[1] + now[0]:
                distance[g[0]] = g[1] + now[0]
                heapq.heappush(q, (distance[g[0]], g[0]))
    result = []
    for i in range(1, n+1):
        if distance[i] != INF:
            result.append(distance[i])
    print(len(result), max(result))
