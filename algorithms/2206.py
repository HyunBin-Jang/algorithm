from collections import deque
import sys

input = sys.stdin.readline
N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(input()))

INF = int(1e9)
d1 = [[INF] * M for _ in range(N)]
d2 = [[INF] * M for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs():
    q = deque([])
    q.append((0,0))
    d1[0][0] = 1
    d2[0][0] = 1

    while q:
        now = q.popleft()
        for i in range(4):
            next_y = now[0] + dy[i]
            next_x = now[1] + dx[i]
            if 0 <= next_y < N and 0 <= next_x < M:
                if graph[next_y][next_x] == '0' and (d1[next_y][next_x] > d1[now[0]][now[1]] + 1 or d2[next_y][next_x] > d2[now[0]][now[1]] + 1):
                    d1[next_y][next_x] = min(d1[next_y][next_x], d1[now[0]][now[1]] + 1)
                    d2[next_y][next_x] = min(d2[next_y][next_x], d2[now[0]][now[1]] + 1)
                    q.append((next_y, next_x))
                elif graph[next_y][next_x] == '1' and d2[next_y][next_x] > d1[now[0]][now[1]] + 1:
                    d2[next_y][next_x] = d1[now[0]][now[1]] + 1
                    q.append((next_y, next_x))

bfs()
result = min(d1[N-1][M-1], d2[N-1][M-1])

if result != INF:
    print(result)
else:
    print(-1)