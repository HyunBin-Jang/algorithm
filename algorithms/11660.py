import sys
N, M = map(int,input().split())
nums = [[]]
for _ in range(N):
    nums.append([0] + list(map(int, input().split())))

d = [[0] * (N + 1) for _ in range(N+1)]

for i in range(1, N + 1):
    for j in range(1, N + 1):
        d[i][j] = d[i-1][j] + d[i][j-1] - d[i-1][j-1] + nums[i][j]

for _ in range(M):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    print(d[x2][y2] - d[x1-1][y2] - d[x2][y1-1] + d[x1-1][y1-1])