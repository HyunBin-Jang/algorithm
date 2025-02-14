from collections import deque
from copy import deepcopy
from itertools import combinations
import sys
input = sys.stdin.readline
N, M, D = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
INF = int(1e9)
def bfs(archors, graph):
    kill_enemy = []
    for archor_x in archors:
        visited = [[False]*M for _ in range(N)]
        q = deque([])
        q.append((N, archor_x, 0))
        nearest = [INF, 0, 0]
        while q:
            now = q.popleft()
            for i in range(4):
                next_y = now[0] + dy[i]
                next_x = now[1] + dx[i]
                distance = now[2] + 1
                if distance > D:
                    break
                if 0 <= next_y < N and 0 <= next_x < M and not visited[next_y][next_x]:
                    if graph[next_y][next_x] == 1:
                        if nearest[0] > distance:
                            nearest = [distance, next_y, next_x]
                        elif nearest[0] == distance and nearest[2] > next_x:
                            nearest = [distance, next_y, next_x]
                    q.append((next_y,next_x,distance))
                    visited[next_y][next_x] = True
        if nearest[0] != INF:
            kill_enemy.append(nearest)
    numofkill = 0
    for e in kill_enemy:
        if graph[e[1]][e[2]] == 1:
            graph[e[1]][e[2]] = 0
            numofkill += 1
    return numofkill

def gameover(graph):
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                return False
    return True
cases = list(combinations([i for i in range(M)], 3))
result = 0
for archors in cases:
    numofkill = 0
    gameboard = deepcopy(graph)
    while not gameover(gameboard):
        numofkill += bfs(archors, gameboard)
        gameboard.pop()
        gameboard = [[0] * M] + gameboard
    result = max(result, numofkill)

print(result)