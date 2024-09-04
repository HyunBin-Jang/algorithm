from collections import deque

n, m = map(int, input().split())
graph = [""]
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
start = [1, 1]

for _ in range(n):
    graph.append(list(map(int,"0" + input())))

queue = deque([])
queue.append(start)
while queue :
    t = queue.popleft()
    print(t)
    for i in range(4):
        ny = t[0] + dy[i]
        nx = t[1] + dx[i]
        if ny < 1 or ny > n or nx < 1 or nx > m:
            continue
        elif int(graph[ny][nx]) == 1:
            queue.append([ny,nx])
            graph[ny][nx] = graph[ny][nx] + graph[t[0]][t[1]]

print(graph[n][m])
