from collections import deque
import sys
input = sys.stdin.readline
n = int(input())

graph = []
for _ in range(n):
    graph.append(list(input()))

INF = int(1e9)
d = [[INF] * n for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(graph, d, n):
    q = deque([])
    q.append((0,0,0))
    d[0][0] = 0
    while q:
        before = q.popleft()
        for i in range(4):
            now_y = before[0] + dy[i]
            now_x = before[1] + dx[i]
            now_black = before[2]
            if 0 <= now_y < n and 0 <= now_x < n:
                if graph[now_y][now_x] == '0' and now_black + 1 < d[now_y][now_x]:
                    d[now_y][now_x] = now_black + 1
                    q.append((now_y, now_x, now_black + 1))
                elif graph[now_y][now_x] == '1' and now_black < d[now_y][now_x]:
                    d[now_y][now_x] = now_black
                    q.append((now_y, now_x, now_black))
bfs(graph, d, n)
print(d[n-1][n-1])