import sys
sys.setrecursionlimit(10**6)
M, N = map(int, input().split())
graph = []
d = [[-1] * N for _ in range(M)]
for _ in range(M):
    graph.append(list(map(int, input().split())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(y, x):
    h = 0
    if y == M-1 and x == N-1:
        return 1
    for i in range(4):
        new_x = x + dx[i]
        new_y = y + dy[i]
        if 0 <= new_x < N and 0 <= new_y < M and graph[y][x] > graph[new_y][new_x]:
            if d[new_y][new_x] != -1:
                h += d[new_y][new_x]
            else:
                h += dfs(new_y,new_x)
    if d[y][x] == -1:
        d[y][x] = h
    return h

print(dfs(0,0))