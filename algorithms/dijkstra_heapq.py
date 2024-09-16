import heapq
INF = int(1e9)

# n 노드의 개수, m 간선의 개수
n, m = map(int, input().split())
# 시작 노드
start = int(input())

graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)           # 최단 거리 테이블

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)
print(distance)