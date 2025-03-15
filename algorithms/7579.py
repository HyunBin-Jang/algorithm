import sys
input = sys.stdin.readline
N, M = map(int, input().split())

memory = list(map(int, input().split()))
cost = list(map(int, input().split()))

C = sum(cost)
d = [0] * (C + 1)

for i in range(N):
    m, c = memory[i], cost[i]
    for j in range(C-c, -1, -1):
        d[j + c] = max(d[j + c], d[j] + m)

result = 0
for i in range(C+1):
    if d[i] >= M:
        result = i
        break
print(result)