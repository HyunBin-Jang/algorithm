from collections import deque
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    A, B, C = map(int,input().split())
    graph[A].append([B, C])
    graph[B].append([A, C])

f1, f2 = map(int, input().split())
def bfs(f1, f2, c):
    visited = [False] * (N+1)
    q = deque([])
    q.append(f1)
    visited[f1] = True
    while q:
        now = q.popleft()
        for g in graph[now]:
            if not visited[g[0]] and g[1] >= c:
                if g[0] == f2:
                    return True
                q.append(g[0])
                visited[g[0]] = True
    return False

start = 0
end = 1000000000
mx = 0
while start <= end:
    mid = (start + end) // 2
    if bfs(f1, f2, mid):
        mx = mid
        start = mid + 1
    else:
        end = mid - 1
print(mx)