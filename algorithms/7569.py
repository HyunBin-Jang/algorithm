from collections import deque
M, N, H = map(int, input().split())
graph = []
riped = 0
empty = 0
first_riped = []
dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

for i in range(H):
    tmp1 = []
    for j in range(N):
        tmp2 = list(map(int, input().split()))
        for k in range(M):
            if tmp2[k] == 1:
                riped += 1
                first_riped.append([i,j,k])
            elif tmp2[k] == -1:
                empty += 1
        tmp1.append(tmp2)
    graph.append(tmp1)

goal_riped = M * N * H - empty
queue = deque([])
result = 0

for f in first_riped:
    queue.append([f[0],f[1],f[2],0])

while queue:
    t = queue.popleft()
    for i in range(6):
        new_z = t[0] + dz[i]
        new_y = t[1] + dy[i]
        new_x = t[2] + dx[i]
        day = t[3] + 1
        if (0 <= new_z < H and 0 <= new_x < M
                and 0 <= new_y < N and graph[new_z][new_y][new_x] == 0):
            graph[new_z][new_y][new_x] = 1
            riped += 1
            queue.append([new_z, new_y, new_x, day])
            if riped == goal_riped:
                result = day
                break

if len(first_riped) == goal_riped:
    print(0)
elif riped == goal_riped:
    print(result)
else:
    print(-1)
