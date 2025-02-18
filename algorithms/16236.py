from collections import deque
import sys
from copy import deepcopy

input = sys.stdin.readline
N = int(input())

graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

shark = []
shark_size = [2, 0]         # [상어 크기, 먹은 물고기 수]
for i in range(N):
    for j in range(N):
        if graph[i][j] == 9:
            shark = [i, j]
            graph[i][j] = 0

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
INF = int(1e9)
def bfs(shark, graph, shark_size):
    visited = [[False] * N for _ in range(N)]
    q = deque([])
    q.append((shark[0], shark[1], 0, []))
    visited[shark[0]][shark[1]] = True
    shortest_fish = [-1,-1, INF, []]
    while q:
        now = q.popleft()
        for i in range(4):
            next_y = now[0] + dy[i]
            next_x = now[1] + dx[i]
            distance = now[2] + 1
            path = deepcopy(now[3])
            if distance > shortest_fish[2]:
                continue
            if 0 <= next_y < N and 0 <= next_x < N and not visited[next_y][next_x]:
                if 0 < graph[next_y][next_x] < shark_size[0]:
                    visited[next_y][next_x] = True
                    path.append((next_y, next_x))
                    q.append((next_y, next_x, distance, path))
                    if distance < shortest_fish[2]:
                        shortest_fish[0] = next_y
                        shortest_fish[1] = next_x
                        shortest_fish[2] = distance
                        shortest_fish[3] = path
                    elif distance == shortest_fish[2]:
                        if next_y < shortest_fish[0]:
                            shortest_fish[0] = next_y
                            shortest_fish[1] = next_x
                            shortest_fish[3] = path
                        elif next_y == shortest_fish[0] and next_x < shortest_fish[1]:
                            shortest_fish[0] = next_y
                            shortest_fish[1] = next_x
                            shortest_fish[3] = path
                elif graph[next_y][next_x] == shark_size[0] or graph[next_y][next_x] == 0:
                    visited[next_y][next_x] = True
                    path.append((next_y, next_x))
                    q.append((next_y, next_x, distance, path))
    if shortest_fish[2] == INF:
        return 0
    else:
        for p in shortest_fish[3]:
            if 0 < graph[p[0]][p[1]] < shark_size[0]:
                graph[p[0]][p[1]] = 0
        shark[0] = shortest_fish[0]
        shark[1] = shortest_fish[1]
        shark_size[1] += 1
        if shark_size[0] == shark_size[1]:
            shark_size[0] += 1
            shark_size[1] = 0
        return shortest_fish[2]

result = 0
while True:
    d = bfs(shark, graph, shark_size)
    if d != 0:
        result += d
    else:
        break
print(result)