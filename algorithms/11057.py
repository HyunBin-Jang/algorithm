N = int(input())

d = [[0] * 10 for _ in range(N)]

for i in range(10):
    d[0][i] = 1

for i in range(1, N):
    for j in range(10):
        d[i][j] = sum(d[i-1][:j+1]) % 10007

print(sum(d[N-1]) % 10007)
