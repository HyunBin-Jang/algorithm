import math
N = int(input())
PN_TF = [True] * (N+1)
PN = []
for i in range(2, int(math.sqrt(N)) + 1):
    if PN_TF[i]:
        for j in range(i+1, N+1):
            if j % i == 0:
                PN_TF[j] = False
for i in range(2, N+1):
    if PN_TF[i]:
        PN.append(i)
d = [0] * (N+1)
d[0] = 1
for p in PN:
    for i in range(p, N+1):
        d[i] += d[i-p]
        d[i] %= 123456789
print(d[N])