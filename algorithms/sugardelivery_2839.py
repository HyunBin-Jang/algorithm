N = int(input())
INF = 5001

d = [INF for _ in range(5001)]

d[5] = 1
d[3] = 1


for i in range(6, 5001):
    d[i] = min(d[i - 3] + 1, d[i - 5] + 1)

if d[N] >= 5001:
    print(-1)
else:
    print(d[N])