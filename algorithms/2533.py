import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
tree = [[] for _ in range(N+1)]

for _ in range(N-1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

visited = [False] * (N+1)
d = [[1, 0] for _ in range(N+1)]     # [얼리 어답터, 아닐때]

def dfs(node):
    for n in tree[node]:
        if not visited[n]:
            visited[n] = True
            dfs(n)
            d[node][0] += min(d[n][0], d[n][1])
            d[node][1] += d[n][0]


visited[1] = True
dfs(1)
print(min(d[1]))