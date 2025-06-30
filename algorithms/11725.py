import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
print = sys.stdout.write

N = int(input())

edge = [[] for _ in range(N+1)]
for _ in range(N-1):
    v1, v2 = map(int, input().split())
    edge[v1].append(v2)
    edge[v2].append(v1)

parent = [0] * (N+1)
visited = [False] * (N+1)

def bfs(n):
    for i in edge[n]:
        if not visited[i]:
            visited[i] = True
            parent[i] = n
            bfs(i)
    return None


visited[1] = True
bfs(1)

for i in range(2, N+1):
    print(str(parent[i]) + "\n")