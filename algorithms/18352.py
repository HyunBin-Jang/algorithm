import sys, heapq
input = sys.stdin.readline
N, M, K, X = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)

INF = int(1e9)
d = [INF] * (N+1)
d[X] = 0

q = []
heapq.heappush(q, (0, X))

while q:
    now = heapq.heappop(q)
    if d[now[1]] < now[0]:
        continue
    for e in graph[now[1]]:
        if d[e] > now[0] + 1:
            d[e] = now[0] + 1
            heapq.heappush(q,(d[e],e))

result = []
for i in range(1,N+1):
    if d[i] == K:
        result.append(i)

if result:
    for r in result:
        print(r)
else:
    print(-1)