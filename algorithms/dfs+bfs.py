from collections import deque

N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)
for i in range(N+1):
    graph[i].sort()

start = V

visited_dfs = []
visited_bfs = [start]

def dfs(s):
    if s not in visited_dfs:
        visited_dfs.append(s)
        for k in graph[s]:
            dfs(k)


def bfs():
    queue = deque([])
    queue.append(start)

    while queue:
        t = queue.popleft()
        for j in graph[t]:
            if j not in visited_bfs:
                queue.append(j)
                visited_bfs.append(j)

dfs(start)
bfs()

print(' '.join(map(str, visited_dfs)))
print(' '.join(map(str, visited_bfs)))

