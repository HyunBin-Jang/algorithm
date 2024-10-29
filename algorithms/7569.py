from collections import deque
M, N, H = map(int, input().split())
graph = []
for _ in range(H):
    g = []
    for _ in range(N):
        g.append(list(map(int, input().split())))
    graph.append(g)
start_x = -1
start_y = -1
start_z = -1
dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]
result = []
def bfs():
    q = deque([])
    q.append([start_z, start_y, start_x, 0])
    mx = 0
    while q:
        t = q.popleft()
        for i in range(6):
            z2 = t[0] + dz[i]
            y2 = t[1] + dy[i]
            x2 = t[2] + dx[i]
            if 0 <= z2 < H and 0 <= y2 < N and 0 <= x2 < M and graph[z2][y2][x2] == 0:
                graph[z2][y2][x2] = 1
                q.append([z2, y2, x2, t[3] + 1])
                mx = max(mx, t[3] + 1)
    result.append(mx)

while True:
    find_0 = False
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if graph[i][j][k] == 0:
                    start_z = i
                    start_y = j
                    start_x = i
                    bfs()
                    find_0 = True
    if not find_0:
        break
print(result)