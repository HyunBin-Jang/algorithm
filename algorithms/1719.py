import sys
input = sys.stdin.readline
n, m = map(int, input().split())

INF = int(1e9)
d = [[INF] * (n+1) for _ in range(n+1)]
graph = [[-1] * (n+1) for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    d[a][b] = c
    d[b][a] = c
    graph[a][b] = b
    graph[b][a] = a
for i in range(n+1):
    d[i][i] = 0

for i in range(1, n+1):
    for j in range(1, n + 1):
        for k in range(1, n + 1):
            if d[j][k] > d[j][i] + d[i][k]:
                d[j][k] = d[j][i] + d[i][k]
                graph[j][k] = graph[j][i]

for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] == -1:
            print('-','',end="")
        else:
            print(graph[i][j],'',end="")
    print()