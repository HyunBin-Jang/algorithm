from collections import deque
from itertools import combinations
import copy

N, M = map(int, input().split())
graph = []
zeros = []         # 처음 0 위치
virus = []         # 처음 2 위치

def safe_zone(new_graph):       # 안전 영역 개수 반환
    num = 0
    for g in new_graph:
        for z in g:
            if z == 0:
                num += 1
    return num


dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
def bfs(start, new_graph):
    q = deque([])
    q.append(start)
    while q:
        t = q.popleft()
        for i in range(4):
            new_y = t[0] + dy[i]
            new_x = t[1] + dx[i]
            if 0 <= new_y < N and 0 <= new_x < M and new_graph[new_y][new_x] == 0:
                new_graph[new_y][new_x] = 2
                q.append([new_y, new_x])

for _ in range(N):
    graph.append(list(map(int, input().split())))
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            zeros.append([i, j])
        elif graph[i][j] == 2:
            virus.append([i, j])
zeros = list(combinations(zeros, 3))      # 0인 위치에 대한 3개 묶음 조합

result = 0
for zero in zeros:
    new_graph = copy.deepcopy(graph)
    for z in zero:
        new_graph[z[0]][z[1]] = 1
    for v in virus:
        bfs(v, new_graph)
    result = max(result, safe_zone(new_graph))
print(result)