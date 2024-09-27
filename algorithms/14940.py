from sys import stdin
from collections import deque
n, m = map(int, stdin.readline().split())
graph = []
goal = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
distance = [[0] * m for _ in range(n)]

for i in range(n):
    g = list(map(int, stdin.readline().split()))
    for j in range(m):
        if g[j] == 2:
            goal.append(i)
            goal.append(j)
    graph.append(g)

visited = [[False for _ in range(m)] for i in range(n)]
def bfs():
    q = deque([])
    q.append(goal)
    visited[goal[0]][goal[1]] = True
    distance[goal[0]][goal[1]] = 0
    while q:
        t = q.popleft()
        for i in range(4):
            y = t[0] - dy[i]
            x = t[1] - dx[i]
            if x < 0 or x >= m or y < 0 or y >= n or visited[y][x]:
                continue
            elif graph[y][x] == 0:
                visited[y][x] = True
            else:
                q.append([y, x])
                visited[y][x] = True
                distance[y][x] = distance[t[0]][t[1]] + 1

bfs()
for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            distance[i][j] = -1
        if graph[i][j] == 0:
            distance[i][j] = 0

for i in range(n):
    for r in distance[i]:
        print(r, '', end = "")
    print()

