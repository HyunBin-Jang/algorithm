from collections import deque
N, L, R = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
def bfs(start_y, start_x, visited):
    q = deque([])
    q.append((start_y, start_x))
    group = [(start_y, start_x)]
    visited[start_y][start_x] = True
    while q:
        now = q.popleft()
        for i in range(4):
            next_y = now[0] + dy[i]
            next_x = now[1] + dx[i]
            if (0 <= next_y < N and 0 <= next_x < N and not visited[next_y][next_x]
                    and L <= abs(graph[now[0]][now[1]] - graph[next_y][next_x]) <= R):
                visited[next_y][next_x] = True
                q.append((next_y, next_x))
                group.append((next_y, next_x))
    total = 0
    for g in group:
        total += graph[g[0]][g[1]]
    new_population = total // len(group)
    for g in group:
        graph[g[0]][g[1]] = new_population
    if len(group) >= 2:
        return True
    else:
        return False



move = True
result = 0
while move:
    move = False
    visited = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                move = bfs(i, j, visited) or move
    if move:
        result += 1
print(result)