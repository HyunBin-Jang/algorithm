import sys
input = sys.stdin.readline
N, M = map(int, input().split())

graph = []
for _ in range(N):
    graph.append(input())

visited = [[False] * M for _ in range(N)]
d = [[0] * M for _ in range(N)]
safe_zone = [False] * (N * M)

for i in range(N):
    for j in range(M):
        d[i][j] = i * M + j

def dfs(y, x):
    if not visited[y][x]:
        visited[y][x] = True
        if graph[y][x] == 'U':
            d[y][x] = dfs(y - 1, x)
        elif graph[y][x] == 'D':
            d[y][x] = dfs(y + 1, x)
        elif graph[y][x] == 'L':
            d[y][x] = dfs(y, x - 1)
        elif graph[y][x] == 'R':
            d[y][x] = dfs(y, x + 1)
    return d[y][x]

result = 0
for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            end_point = dfs(i, j)
            if not safe_zone[end_point]:
                safe_zone[end_point] = True
                result += 1

print(result)