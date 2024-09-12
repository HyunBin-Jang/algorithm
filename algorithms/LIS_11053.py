N = int(input())
p = list(map(int, input().split()))
d = [1] * N
result = 0

for i in range(N):
    for j in range(i):
        if p[i] > p[j]:
            d[i] = max(d[i], d[j] + 1)



print(max(d))

