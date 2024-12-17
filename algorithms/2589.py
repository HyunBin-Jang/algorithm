from collections import deque
N, M = map(int, input().split())
graph = []
land = []
for _ in range(N):
    graph.append(input())

for i in range(N):
    for j in range(M):
        if graph[i][j] == 'L':
            land.append([i, j])

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

def bfs(start):
    visited = [[False] * M for _ in range(N)]
    q = deque([])
    q.append(start + [0])
    mx = 0
    visited[start[0]][start[1]] = True
    while q:
        t = q.popleft()
        for i in range(4):
            new_y = t[0] + dy[i]
            new_x = t[1] + dx[i]
            if 0 <= new_y < N and 0 <= new_x < M and graph[new_y][new_x] == 'L' and not visited[new_y][new_x]:
                visited[new_y][new_x] = True
                mx = max(mx, t[2] + 1)
                q.append([new_y,new_x, t[2] + 1])
    return mx

result = 0
for l in land:
    result = max(result, bfs(l))
print(result)