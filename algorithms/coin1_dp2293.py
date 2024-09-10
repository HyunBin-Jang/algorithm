n, k = map(int,input().split())

coins = []
d = [0] * (k+1)

for _ in range(n):
    coins.append(int(input()))

d[0] = 1

for c in coins:
    for j in range(c, k+1):
      if d[j - c] != 0:
          d[j] += d[j-c]

print(d[k])