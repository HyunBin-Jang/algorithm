from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []

for _ in range(n):
    graph.append(list(map(int,input().split())))

visited = [[False] * m for _ in range(n)]

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

def bfs(start_y, start_x):
    visited[start_y][start_x] = True
    q = deque([])
    q.append((start_y, start_x))
    size = 1
    while q:
        before = q.popleft()
        for i in range(4):
            new_y = before[0] + dy[i]
            new_x = before[1] + dx[i]
            if 0 <= new_y < n and 0 <= new_x < m and not visited[new_y][new_x] and graph[new_y][new_x] == 1:
                visited[new_y][new_x] = True
                size += 1
                q.append((new_y, new_x))
    return size

num_pictures = 0
mx_size = 0
for i in range(n):
    for j in range(m):
        if not visited[i][j] and graph[i][j] == 1:
            num_pictures += 1
            mx_size = max(mx_size, bfs(i, j))

print(num_pictures)
print(mx_size)