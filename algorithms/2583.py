from collections import deque
M, N, K = map(int, input().split())
graph = [[0 for _ in range(N)] for _ in range(M)]
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            graph[j][i] = 1

num_area = 0
area = []
start_x = -1
start_y = -1
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def bfs():
    n = 1
    q = deque([])
    q.append([start_y, start_x])
    graph[start_y][start_x] = 1
    while q:
        t = q.popleft()
        for i in range(4):
            if 0 <= t[0] + dy[i] < M and 0 <= t[1] + dx[i] < N and graph[t[0] + dy[i]][t[1] + dx[i]] == 0:
                q.append([t[0] + dy[i], t[1] + dx[i]])
                graph[t[0] + dy[i]][t[1] + dx[i]] = 1
                n += 1
    area.append(n)

for i in range(M):
    for j in range(N):
        if graph[i][j] == 0:
            start_x = j
            start_y = i
            num_area += 1
            bfs()
area.sort()
print(num_area)
for a in area:
    print(a,'',end="")