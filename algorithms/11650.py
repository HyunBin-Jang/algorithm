import sys
N = int(input())
xy = [[] for i in range(200001)]

for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    xy[x + 100000].append(y)

for i in range(200001):
    if xy[i]:
        xy[i].sort()
        for yy in xy[i]:
            print(i - 100000, yy)

