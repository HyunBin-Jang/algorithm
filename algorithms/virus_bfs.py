from collections import deque

n = int(input())
pair_num = int(input())

pair = []
start = 0
visited = []

for i in range(n):
    p = list(map(int, input().split()))
    if p[0]==1 or p[1]==1:
        start = p
    pair.append(p)

def bfs():
    queue = deque([])
    queue.append(start)

    while queue:
        t = queue.popleft()
        if t[1] not in visited:
            visited.append(t[1])
            for _ in range(n):
                p = list(map(int, input().split()))
                if p[0] == 1 or p[1] == 1:





