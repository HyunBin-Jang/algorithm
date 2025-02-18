import sys
input = sys.stdin.readline

N = int(input())
INF = int(1e9)
d = [[INF]*(N+1) for _ in range(N+1)]

for i in range(N+1):
    d[i][i] = 0

while True:
    n, m = map(int, input().split())
    if n == -1 and m == -1:
        break
    d[n][m] = 1
    d[m][n] = 1

for i in range(1, N+1):
    for j in range(1, N+1):
        for k in range(1, N+1):
            d[j][k] = min(d[j][k], d[j][i] + d[i][k])

for i in range(N+1):
    for j in range(N+1):
        if d[i][j] == INF:
            d[i][j] = 0
candidate = []
mn = INF
for i in range(1, N+1):
    if max(d[i]) < mn:
        candidate = [i]
        mn = max(d[i])
    elif max(d[i]) == mn:
        candidate.append(i)
print(mn, len(candidate))
for c in candidate:
    print(c,'', end="")