import heapq
from heapq import heappop

M, N = map(int, input().split())
graph = []
for _ in range(N):
    inp = input()
    tmp = []
    for i in inp:
        tmp.append(int(i))
    graph.append(tmp)
INF = 10 ** 9
d = [[INF] * M for _ in range(N)]
visited = [[False] * M for _ in range(N)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def dijkstra():
    q = []
    heapq.heappush(q, [graph[0][0],0,0])
    d[0][0] = graph[0][0]
    while q:
        t = heappop(q)
        for i in range(4):
            x = t[1] + dx[i]
            y = t[2] + dy[i]
            if 0 <= x < M and 0 <= y < N and not visited[y][x]:
                visited[y][x] = True
                d[y][x] = t[0] + graph[y][x]
                heapq.heappush(q,[d[y][x], x, y])
dijkstra()
print(d[N-1][M-1])