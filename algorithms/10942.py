import sys
input = sys.stdin.readline

N = int(input())
nums = [0] + list(map(int, input().split()))
d = [[False] * (N+1) for _ in range(N+1)]

for i in range(N+1):
    d[i][i] = True

# d[i][j] = d[i+1][j-1] and nums[i] == nums[j]
for j in range(1, N+1):
    for i in range(1, N+1):
        if i + 1 == j:
            d[i][j] = nums[i] == nums[j]
        elif i + 1 > j-1:
            continue
        else:
            d[i][j] = d[i+1][j-1] and nums[i] == nums[j]

M = int(input())
for _ in range(M):
    S, E = map(int, input().split())
    if d[S][E]:
        print(1)
    else:
        print(0)


