from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
graph = []

for _ in range(N):
    graph.append(list(map(int, input().split())))
mx = 0
for n in range(N):
    mx = max(mx, max(graph[n]))

dx = [1 , -1, 0, 0]
dy = [0, 0 , 1, -1]
def bfs(start, criteria, visited):
    q = deque([start])
    visited[start[0]][start[1]] = True
    while q:
        before = q.popleft()
        for i in range(4):
            new_y = before[0] + dy[i]
            new_x = before[1] + dx[i]
            if (0 <= new_x < N and 0 <= new_y < N
                    and not visited[new_y][new_x]) and graph[new_y][new_x] > criteria:
                q.append((new_y, new_x))
                visited[new_y][new_x] = True

result = 0
for c in range(mx):
    safe_area = 0
    visited = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and graph[i][j] > c:
                bfs((i,j), c, visited)
                safe_area += 1
    result = max(result, safe_area)

print(result)