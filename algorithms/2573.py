from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = []

numOfNonZero = 0
for _ in range(N):
    tmp = list(map(int, input().split()))
    for i in range(M):
        if tmp[i] > 0:
            numOfNonZero += 1
    graph.append(tmp)


dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

def over_a_year(start_y, start_x):
    dv = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    visited[start_y][start_x] = True
    q = deque([])
    q.append((start_y, start_x))
    new_zero = 0
    while q:
        before = q.popleft()
        value = 0
        for i in range(4):
            y = before[0] + dy[i]
            x = before[1] + dx[i]
            if graph[y][x] <= 0:
                value += 1
            elif not visited[y][x]:
                visited[y][x] = True
                q.append((y,x))
        dv[before[0]][before[1]] = value
    for i in range(N):
        for j in range(M):
            if graph[i][j] > 0:
                graph[i][j] -= dv[i][j]
                if graph[i][j] <= 0:
                    new_zero += 1
    return new_zero

def check_glacier(start_y, start_x):
    visited = [[False] * M for _ in range(N)]
    visited[start_y][start_x] = True
    q = deque([])
    q.append((start_y, start_x))
    nonzero = 1
    while q:
        while q:
            before = q.popleft()
            for i in range(4):
                y = before[0] + dy[i]
                x = before[1] + dx[i]
                if graph[y][x] > 0 and not visited[y][x]:
                    nonzero += 1
                    visited[y][x] = True
                    q.append((y, x))
    return nonzero

def find_nonzero():
    for i in range(N):
        for j in range(M):
            if graph[i][j] > 0:
                return i, j
    return 0, 0

time = 0
while True:
    i, j = find_nonzero()
    numOfNonZero -= over_a_year(i, j)
    time += 1

    if numOfNonZero == 0:
        time = 0
        break

    i, j = find_nonzero()
    if not (numOfNonZero == check_glacier(i, j)):
        break

print(time)