N = int(input())
cost = [[]]
for _ in range(N):
    cost.append(list(map(int, input().split())))
d = [[0, 0, 0] for _ in range(N + 1)]   # 0:R 1:G 2:B  lowest cost


d[1][0] += cost[1][0]
d[1][1] += cost[1][1]
d[1][2] += cost[1][2]

for i in range(2, N + 1):
    if i == 2:
        d[i][0] = min(d[1][1], d[1][2]) + cost[i][0]
        d[i][1] = min(d[1][0], d[1][2]) + cost[i][1]
        d[i][2] = min(d[1][0], d[1][1]) + cost[i][2]
    else:
        d[i][0] = min(d[i-1][1], d[i-1][2]) + cost[i][0]
        d[i][1] = min(d[i-1][0], d[i-1][2]) + cost[i][1]
        d[i][2] = min(d[i-1][0], d[i-1][1]) + cost[i][2]

print(min(d[N]))