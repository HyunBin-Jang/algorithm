from collections import deque
n = int(input())
a, b = map(int, input().split())
m = int(input())

R = [[] for _ in range(n + 1)]

for _ in range(m):
    x, y = map(int, input().split())
    R[x].append(y)
    R[y].append(x)

visited = []

def bfs(start, end):
    q = deque([])
    result = 0
    q.append([start, result])
    visited.append(start)
    while q:
        t = q.popleft()
        for i in R[t[0]]:
            if i == end:
                return t[1] + 1
            elif i not in visited:
                q.append([i, t[1] + 1])
                visited.append(i)
    return -1

print(bfs(a, b))

