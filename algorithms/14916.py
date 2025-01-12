N = int(input())
d = [0] * 100001
d[2] = 1
d[4] = 2
d[5] = 1
for i in range(5, N+1):
    if d[i-5] != 0 and d[i-2] != 0:
        d[i] = min(d[i-5], d[i-2]) + 1
    elif d[i-5] != 0:
        d[i] = d[i-5] + 1
    elif d[i-2] != 0:
        d[i] = d[i-2] + 1
if d[N] == 0:
    print(-1)
else:
    print(d[N])