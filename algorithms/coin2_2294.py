n, k = map(int, input().split())
coins = []
d = [10001]*(k+1)
d[0] = 0

for _ in range(n):
    coins.append(int(input()))


for i in range(k+1):
    for c in coins:
        if i - c >= 0:
            d[i] = min(d[i], d[i-c] + 1)

if d[k] == 10001:
    print(-1)
else:
    print(d[k])
