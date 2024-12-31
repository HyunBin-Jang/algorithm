from collections import deque
from copy import deepcopy

N = int(input())
graph = []
for _ in range(N):
    graph.append(list(input()))

graph1 = deepcopy(graph)
graph2 = deepcopy(graph)
for i in range(N):
    for j in range(N):
        if graph2[i][j] == 'G':
            graph2[i][j] = 'R'

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(g, start_y, start_x, target):
    queue = deque([])
    queue.append([start_y,start_x])
    while queue:
        old = queue.popleft()
        for i in range(4):
            new_y = old[0] + dy[i]
            new_x = old[1] + dx[i]
            if 0 <= new_y < N and 0 <= new_x < N and g[new_y][new_x] == target:
                g[new_y][new_x] = '0'
                queue.append([new_y, new_x])

result1 = 0
for i in range(N):
    for j in range(N):
        if graph1[i][j] != '0':
            bfs(graph1,i,j,graph1[i][j])
            result1 += 1

result2 = 0
for i in range(N):
    for j in range(N):
        if graph2[i][j] != '0':
            bfs(graph2,i,j,graph2[i][j])
            result2 += 1

print(result1, result2)