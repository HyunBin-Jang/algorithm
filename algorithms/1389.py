N, M = map(int,input().split())
graph = []

INF = int(1e9)
d = [[INF] * (N+1) for _ in range(N+1)]

for _ in range(M):
    A, B = map(int, input().split())
    d[A][B] = 1
    d[B][A] = 1

for i in range(N+1):
    d[i][i] = 0

for i in range(1, N+1):
    for j in range(1, N+1):
        for k in range(1, N+1):
            d[j][k] = min(d[j][k], d[j][i] + d[i][k])

result = []
for i in range(N+1):
    result.append(sum(d[i][1:]))

min_idx = 0
for i in range(1, N+1):
    if result[min_idx] > result[i]:
        min_idx = i
print(min_idx)