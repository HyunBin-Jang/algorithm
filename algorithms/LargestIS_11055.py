N = int(input())

seq = list(map(int, input().split()))
d = seq[:]

for i in range(N):
    for j in range(i):
        if seq[i] > seq[j]:
            d[i] = max(d[i], d[j] + seq[i])


print(max(d))
