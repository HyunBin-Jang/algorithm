import sys, heapq
input = sys.stdin.readline
N = int(input())
M = int(input())

INF = 10**9
distance = [INF] * (N + 1)

graph = [[] for i in range(N+1)]
for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((v,w))

start, end = map(int, input().split())

distance[start] = 0
q = []
heapq.heappush(q, (0, start))

while q:
    now = heapq.heappop(q)
    if now[1] == end:             # 도착지 처리시 바로 반복문 종료로 최적화
        break
    if now[0] > distance[now[1]]:
        continue
    for e in graph[now[1]]:
        if e[1] + now[0] < distance[e[0]]:
            distance[e[0]] = e[1] + now[0]
            heapq.heappush(q, (distance[e[0]], e[0]))
print(distance[end])