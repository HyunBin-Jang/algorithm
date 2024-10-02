import sys
from collections import deque
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
sys.setrecursionlimit(10**6)
N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(input())

visited = []
def bfs():
    q = deque([])
    distance = 1
    q.append([0, 0, 1])
    visited.append([0, 0])
    while q:
        t = q.popleft()
        for i in range(4):
            y = t[0] - dy[i]
            x = t[1] - dx[i]
            d = t[2] + 1
            if y < 0 or y >= N or x < 0 or x >= M or graph[y][x] == '0' or [y, x] in visited:
                continue
            elif y == N-1 and x == M - 1:
                return d
            else:
                q.append([y, x, d])
                visited.append([y, x])

print(bfs())