N = int(input())

d0 = [0] * (N+1)
d1 = [1] * (N+1)

d1[1] = 1
for n in range(2, N+1):
    d0[n] = d0[n-1] + d1[n-1]
    d1[n] = d0[n-1]
print(d1[N] + d0[N])