import sys, heapq
input = sys.stdin.readline

T = int(input())
INF = int(1e9)
def dijkstra(d, graph, s):
    q = []
    d[s] = 0
    heapq.heappush(q, (s, 0))
    while q:
        now = heapq.heappop(q)
        if d[now[0]] < now[1]:
            continue
        for edge in graph[now[0]]:
            next_node, cost = edge
            if d[next_node] > now[1] + cost:
                d[next_node] = now[1] + cost
                heapq.heappush(q, (next_node, d[next_node]))


for _ in range(T):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    cost_gh = 0
    for _ in range(m):
        a, b, d = map(int, input().split())
        graph[a].append((b, d))
        graph[b].append((a, d))
        if (a == g and b == h) or (a == h and b == g):
            cost_gh = d

    d1 = [INF] * (n+1)
    d2 = [INF] * (n+1)
    d3 = [INF] * (n+1)
    dijkstra(d1, graph, s)
    dijkstra(d2, graph, g)
    dijkstra(d3, graph, h)

    result = []
    for _ in range(t):
        c = int(input())
        case1 = d1[g] + cost_gh + d3[c]
        case2 = d1[h] + cost_gh + d2[c]
        if case1 == d1[c] or case2 == d1[c]:
            result.append(c)
    result.sort()
    for n in result:
        print(n,"", end="")
