from collections import deque
import sys
input = sys.stdin.readline
n = int(input())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

INF = int(1e9)
d = [[INF] * n for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(graph, d, n):
    q = deque([])
    q.append((0,0))
    d[0][0] = graph[0][0]
    while q:
        before = q.popleft()
        for i in range(4):
            now_y = before[0] + dy[i]
            now_x = before[0] + dx[i]
            if 0 <= now_y < n and 0 <= now_x < n:
