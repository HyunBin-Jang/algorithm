n, m, r = map(int, input().split())
t = [0] + list(map(int, input().split()))

INF = int(1e9)
d = [[INF] * (n+1) for _ in range(n+1)]

for _ in range(r):
    a, b, l = map(int, input().split())
    d[a][b] = l
    d[b][a] = l

for i in range(1, n+1):
    d[i][i] = 0

for i in range(1, n + 1):
    for j in range(1, n + 1):
        for k in range(1, n + 1):
            d[j][k] = min(d[j][k], d[j][i] + d[i][k])

result = []
for i in range(1, n+1):
    items = 0
    for j in range(1, n+1):
        if d[i][j] <= m:
            items += t[j]
    result.append(items)

print(max(result))