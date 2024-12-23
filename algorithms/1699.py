import math
N = int(input())
d = [0] + [100001] * N
for i in range(1, N+1):
    for j in range(1, int(math.sqrt(i)) + 1):
        d[i] = min(d[i], d[i-j**2] + 1)
print(d[N])