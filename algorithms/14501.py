N = int(input())
schedule = []
for _ in range(N):
    schedule.append(list(map(int, input().split())))
d = [0] * (N + 1)

for i in range(N):
    if i + schedule[i][0] <= N:
        d[i + schedule[i][0]] = max(d[i + schedule[i][0]], d[i] + schedule[i][1])
    d[i + 1] = max(d[i + 1], d[i])
print(d[N])