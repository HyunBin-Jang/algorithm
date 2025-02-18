from collections import deque
import sys

input = sys.stdin.readline
N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

INF = int(1e9)

dx = [1, -1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, 1, -1, 1, -1, 1, -1]
def bfs(start_y, start_x, graph):
    visited = [[False] * M for _ in range(N)]
    q = deque([])
    q.append((start_y, start_x, 0))
    visited[start_y][start_x] = True
    min_distance = INF
    while q:
        now = q.popleft()
        for i in range(8):
            next_y = now[0] + dy[i]
            next_x = now[1] + dx[i]
            distance = now[2] + 1
            if 0 <= next_y < N and 0 <= next_x < M and not visited[next_y][next_x]:
                visited[next_y][next_x] = True
                q.append((next_y, next_x, distance))
                if graph[next_y][next_x] == 1:
                    min_distance = min(min_distance, distance)
    return min_distance

result = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            continue
        result = max(result, bfs(i, j, graph))
print(result)