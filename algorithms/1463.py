N = int(input())
INF = 10**6
d = [INF]*(N+1)
d[1] = 0
for i in range(1, N+1):
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)
    if i % 2 == 0:
        d[i] = min(d[i],d[i // 2] + 1)
    d[i] = min(d[i],d[i-1] + 1)
print(d[N])