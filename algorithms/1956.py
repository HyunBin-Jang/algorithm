import sys
input = sys.stdin.readline
V, E = map(int, input().split())
INF = int(1e9)
d = [[INF]*(V+1) for _ in range(V+1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    d[a][b] = min(d[a][b], c)

for i in range(1, V+1):
    d[i][i] = 0


for i in range(1, V+1):
    for j in range(1, V+1):
        for k in range(1, V+1):
            d[j][k] = min(d[j][k], d[j][i] + d[i][k])

result = INF
for i in range(1, V+1):
    for j in range(1, V+1):
        if i == j:
            continue
        if d[i][j] != INF and d[j][i] != INF:
            result = min(result, d[i][j] + d[j][i])
if result == INF:
    print(-1)
else:
    print(result)