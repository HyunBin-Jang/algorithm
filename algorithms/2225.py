N, K = map(int, input().split())

d = [[0 for _ in range(K+1)] for _ in range(N+1)]

d[0][0] = 1

for i in range(N + 1):
    for j in range(1, K + 1):
        d[i][j] = d[i][j - 1]
        if i > 0:
            d[i][j] += d[i - 1][j]
        d[i][j] %= 1000000000

print(d[N][K])