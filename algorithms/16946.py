from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(input()))

parent = [[-1] * M for _ in range(N)]
d = []

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(y, x, n):
    q = deque([])
    q.append((y, x))
    parent[y][x] = n
    numofzero = 1

    while q:
        now = q.popleft()
        for i in range(4):
            next_y = now[0] + dy[i]
            next_x = now[1] + dx[i]
            if 0 <= next_y < N and 0 <= next_x < M and parent[next_y][next_x] == -1 and graph[next_y][next_x] == '0':
                numofzero += 1
                q.append((next_y, next_x))
                parent[next_y][next_x] = n
    d.append(numofzero)

p_num = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] == '0' and parent[i][j] == -1:
            bfs(i, j, p_num)
            p_num += 1

result = [[0] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if graph[i][j] == '1':
            sums = 1
            parents = []
            for k in range(4):
                y = i + dy[k]
                x = j + dx[k]
                if 0 <= y < N and 0 <= x < M and graph[y][x] == '0' and parent[y][x] not in parents:
                    sums += d[parent[y][x]] % 10
                    parents.append(parent[y][x])
            result[i][j] = sums % 10

for i in range(N):
    for j in range(M):
        print(result[i][j], end="")
    print()
