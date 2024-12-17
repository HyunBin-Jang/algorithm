n = int(input())
d = [1] * n
box = list(map(int, input().split()))

for i in range(n):
    for j in range(i+1, n):
        if box[i] < box[j]:
            d[j] = max(d[j], d[i] + 1)

d.sort()
print(d[n-1])