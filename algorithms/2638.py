from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

cheese_num = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            cheese_num += 1

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
def bfs():
    visited = [[False] * M for _ in range(N)]
    q = deque([])
    q.append((0,0))
    graph[0][0] = -1
    while q:
        before = q.popleft()
        for i in range(4):
            y = before[0] + dy[i]
            x = before[1] + dx[i]
            if 0 <= y < N and 0 <= x < M and not visited[y][x] and graph[y][x] != 1:
                graph[y][x] = -1
                visited[y][x] = True
                q.append((y, x))

def melt():
    melting = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                air = 0
                for k in range(4):
                    y = i + dy[k]
                    x = j + dx[k]
                    if 0 <= y < N and 0 <= x < M and graph[y][x] == -1:
                        air += 1
                if air >= 2:
                    graph[i][j] = 0
                    melting += 1
    return melting

time = 0
while cheese_num != 0:
    bfs()
    cheese_num -= melt()
    time += 1

print(time)