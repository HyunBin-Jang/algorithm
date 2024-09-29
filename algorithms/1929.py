import math
M, N = map(int, input().split())

d = [True] * (N + 1)
d[0] = False
d[1] = False

for i in range(2, int(math.sqrt(N)) + 1):
    j = 2
    while i * j <= N:
        d[i * j] = False
        j += 1

for i in range(M, N + 1):
    if d[i]:
        print(i)
