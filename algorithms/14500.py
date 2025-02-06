from collections import deque
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
graph = []

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for _ in range(N):
    graph.append(list(map(int, input().split())))


def bfs(graph, y, x):
    mx_result = 0
    q = deque([])
    q.append((y,x,1, graph[y][x], 0))          # y, x, 현재 몇 번째 블럭 까지 선택, 선택된 블럭 들의 합, 선택된 방향
    while q:
        before = q.popleft()
        for i in range(4):
            if i == (before[4] + 2) % 4 and before[2] != 1:
                continue
            now_y = before[0] + dy[i]
            now_x = before[1] + dx[i]
            if 0 <= now_y < N and 0 <= now_x < M:
                if before[2] == 3:
                    mx_result = max(mx_result, before[3] + graph[now_y][now_x])
                else:
                    q.append((now_y, now_x, before[2]+1, before[3] + graph[now_y][now_x], i))
    return mx_result

def shape_5(graph, y, x):
    mx_result = 0
    shapes = [(0,1,2), (0, 2, 3), (0, 1, 3), (1, 2, 3)]
    for shape in shapes:
        total = graph[y][x]
        for i in shape:
            if 0 <= y + dy[i] < N and 0 <= x + dx[i] < M:
                total += graph[y + dy[i]][x + dx[i]]
        mx_result = max(mx_result, total)
    return mx_result
result = 0
for i in range(N):
    for j in range(M):
        result = max(result, bfs(graph, i, j), shape_5(graph, i, j))

print(result)