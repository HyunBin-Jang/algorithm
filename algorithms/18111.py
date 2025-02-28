import sys
input = sys.stdin.readline

N, M, B = map(int, input().split())
ground = []

mn = 256
mx = 0
total = 0
sums = []
for i in range(N):
    tmp = list(map(int, input().split()))
    mn = min(mn, min(tmp))
    mx = max(mx, max(tmp))
    total += sum(tmp)
    sums.append(sum(tmp))
    tmp.sort()
    ground.append(tmp)

size = N * M
time = int(1e9)
height = 0

d = [[-1, 0] for _ in range(N)]

for n in range(mn, mx+1):
    t = 0
    if total + B < n * size:
        continue
    for i in range(N):
        if d[i][0] != -1:
            t += n * (d[i][0]+1) - d[i][1]
        for j in range(d[i][0]+1, M):
            if ground[i][j] < n:
                t += (n - ground[i][j])
                d[i][0] = j
                d[i][1] += ground[i][j]
            elif ground[i][j] > n:
                t += (sums[i] - d[i][1] - n * (M - d[i][0] - 1)) * 2
                break
            else:
                d[i][0] = j
                d[i][1] += ground[i][j]
    if t <= time:
        time = t
        height = n

print(time, height)