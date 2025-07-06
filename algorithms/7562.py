from collections import deque
import sys
input = sys.stdin.readline

T = int(input())

dy = [2, 2, 1, 1, -1, -1, -2, -2]
dx = [1, -1, 2, -2, 2, -2, 1, -1]

def bfs(start_y, start_x, end_y, end_x, I):
    q = deque([])
    q.append((start_y, start_x, 0))
    visited = [[False] * I for _ in range(I)]
    visited[start_y][start_x] = True

    while q:
        before = q.popleft()
        for i in range(8):
            y = before[0] + dy[i]
            x = before[1] + dx[i]
            m = before[2] + 1
            if 0 <= y < I and 0 <= x < I and not visited[y][x]:
                visited[y][x] = True
                if y == end_y and x == end_x:
                    return m
                else:
                    q.append((y,x,m))

for _ in range(T):
    I = int(input())
    start_y, start_x = map(int, input().split())
    end_y, end_x = map(int, input().split())

    if start_y == end_y and start_x == end_x:
        print(0)
    else:
        print(bfs(start_y, start_x, end_y, end_x, I))


