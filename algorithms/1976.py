from collections import deque
N = int(input())
M = int(input())
graph = [[]]
for _ in range(N):
    graph.append([0] + list(map(int, input().split())))
plan = list(map(int, input().split()))

def bfs(start, end, visited):
    if start == end:
        return True
    q = deque([])
    q.append(start)
    visited[start] = True
    while q:
        t = q.popleft()
        if graph[t][end] == 1:
            return True
        for i in range(1, N + 1):
            if graph[t][i] == 1 and not visited[i]:
                q.append(i)
                visited[i] = True
    return False

result = True
for i in range(M-1):
    visited = [False] * (N + 1)
    if not bfs(plan[i], plan[i + 1], visited):
        result = False
        break

if result:
    print("YES")
else:
    print("NO")
