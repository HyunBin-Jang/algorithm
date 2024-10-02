from sys import stdin
N = int(input())
XY = [[] for _ in range(200001)]
for _ in range(N):
    x, y = map(int, stdin.readline().split())
    XY[y + 100000].append(x)

for i in range(200001):
    if XY[i]:
        XY[i].sort()
        for j in XY[i]:
            print(j, i - 100000)