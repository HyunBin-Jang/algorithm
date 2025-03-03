N = int(input())

d = [0] * (N+1)
d[0] = 1
if N >= 2:
    d[2] = 3
for i in range(4, N+1):
    d[i] += d[i-2] * 3
    for j in range(4,i+1,2):
        d[i] += d[i-j] * 2
print(d[N])