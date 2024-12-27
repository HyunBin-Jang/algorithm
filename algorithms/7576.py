from collections import deque
M, N = map(int, input().split())
graph = []
riped = 0
empty = 0
first_riped = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for i in range(N):
    tmp = list(map(int, input().split()))
    for j in range(M):
        if tmp[j] == 1:
            riped += 1
            first_riped.append([i,j])
        elif tmp[j] == -1:
            empty += 1
    graph.append(tmp)

goal_riped = M * N - empty
queue = deque([])
result = 0
for f in first_riped:
    queue.append([f[0],f[1],0])
while queue:
    t = queue.popleft()
    for i in range(4):
        new_x = t[1] + dx[i]
        new_y = t[0] + dy[i]
        day = t[2] + 1
        if 0 <= new_x < M and 0 <= new_y < N and graph[new_y][new_x] == 0:
            graph[new_y][new_x] = 1
            riped += 1
            queue.append([new_y, new_x, day])
            if riped == goal_riped:
                result = day
                break
if len(first_riped) == goal_riped:
    print(0)
elif riped == goal_riped:
    print(result)
else:
    print(-1)
