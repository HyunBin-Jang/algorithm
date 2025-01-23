N = int(input())
graph = []

for _ in range(N):
    graph.append(list(map(int, input().split())))

INF = int(1e9)
d = [[INF]*N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if graph[i][j] != 0:
            d[i][j] = graph[i][j]


for i in range(N):
    for j in range(N):
        for k in range(N):
            d[j][k] = min(d[j][k], d[j][i] + d[i][k])

for i in range(N):
    for j in range(N):
        if d[i][j] < INF:
            print(1,'', end="")
        else:
            print(0,'', end="")
    print()