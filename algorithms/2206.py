from collections import deque
import sys

input = sys.stdin.readline
N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))


INF = int(1e9)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def bfs():
    q = deque([])
    q.append((0,0,1,False))
    distance = INF
    while q:
        now = q.popleft()
        for i in range(N):
            next_y = now[0] + dy[i]
            next_x = now[1] + dx[i]
            distance = now[2] + 1
            if 0 <= next_y < N and 0 <= next_x < M and not visited

