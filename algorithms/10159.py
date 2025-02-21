import sys
input = sys.stdin.readline
N = int(input())
M = int(input())

INF = int(1e9)
d = [[INF] * (N+1) for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    d[a][b] = 1
for i in range(1, N+1):
    d[i][i] = 0

for i in range(1, N+1):
    for j in range(1, N+1):
        for k in range(1, N + 1):
            d[j][k] = min(d[j][k], d[j][i] + d[i][k])

for i in range(1, N+1):
    result = 0
    for j in range(1, N + 1):
        if d[i][j] == INF and d[j][i] == INF:
            result += 1
    print(result)