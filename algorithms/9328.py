from collections import deque
import sys
input = sys.stdin.readline

T = int(input())

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

def bfs(graph, key, start_y, start_x, h, w, visited):
    document = 0
    find_key = False
    q = deque([])
    visited[start_y][start_x] = True
    if graph[start_y][start_x] == '.':
        q.append((start_y, start_x))
    elif graph[start_y][start_x] == '$':
        q.append((start_y, start_x))
        graph[start_y][start_x] = '.'
        document += 1
    elif graph[start_y][start_x].islower():
        q.append((start_y, start_x))
        key[ord(graph[start_y][start_x]) - 97] = True
        graph[start_y][start_x] = '.'
        find_key = True
    elif graph[start_y][start_x].isupper() and key[ord(graph[start_y][start_x]) - 65]:
        q.append((start_y, start_x))
        graph[start_y][start_x] = '.'

    while q:
        before_y, before_x = q.popleft()
        for i in range(4):
            next_y = before_y + dy[i]
            next_x = before_x + dx[i]

            if 0 <= next_y < h and 0 <= next_x < w and not visited[next_y][next_x]:
                if graph[next_y][next_x] == '*':
                    visited[next_y][next_x] = True
                    continue
                elif graph[next_y][next_x] == '.':
                    q.append((next_y, next_x))
                elif graph[next_y][next_x] == '$':
                    graph[next_y][next_x] = '.'
                    q.append((next_y, next_x))
                    document += 1
                elif graph[next_y][next_x].islower():
                    key[ord(graph[next_y][next_x]) - 97] = True
                    graph[next_y][next_x] = '.'
                    q.append((next_y, next_x))
                    find_key = True
                elif graph[next_y][next_x].isupper():
                    if key[ord(graph[next_y][next_x]) - 65]:
                        graph[next_y][next_x] = '.'
                        q.append((next_y, next_x))
                visited[next_y][next_x] = True
    return find_key, document

def border(graph, start, h, w):
    for i in range(w):
        if graph[0][i] != '*':
            start.append((0, i))
        if graph[h-1][i] != '*':
            start.append((h-1, i))
    for i in range(1, h-1):
        if graph[i][0] != '*':
            start.append((i, 0))
        if graph[i][w-1] != '*':
            start.append((i, w-1))

for _ in range(T):
    h, w = map(int, input().split())
    key = [False] * 26
    graph = []
    start = []
    for _ in range(h):
        graph.append(list(input()))
    keys = input().rstrip()
    if keys != "0":
        for k in keys:
            key[ord(k) - 97] = True
    border(graph, start, h, w)
    find_key = True
    result = 0
    while find_key:
        find_key = False
        visited = [[False] * w for _ in range(h)]
        for s in start:
            f, d = bfs(graph, key, s[0], s[1], h, w, visited)
            find_key = f or find_key
            result += d
    print(result)
