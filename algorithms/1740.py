import sys
input = sys.stdin.readline

N = int(input())
cost = []
for _ in range(N):
    cost.append(list(map(int, input().split())))
INF = int(1e9)

d1 = [[0, 0, 0] for _ in range(N)]
d1[0][0] = cost[0][0]
d1[0][1] = INF
d1[0][2] = INF

d2 = [[0, 0, 0] for _ in range(N)]
d2[0][0] = INF
d2[0][1] = cost[0][1]
d2[0][2] = INF

d3 = [[0, 0, 0] for _ in range(N)]
d3[0][0] = INF
d3[0][1] = INF
d3[0][2] = cost[0][2]
for i in range(1, N):
    d1[i][0] = min(d1[i - 1][1], d1[i - 1][2]) + cost[i][0]
    d1[i][1] = min(d1[i - 1][0], d1[i - 1][2]) + cost[i][1]
    d1[i][2] = min(d1[i - 1][0], d1[i - 1][1]) + cost[i][2]
    d2[i][0] = min(d2[i - 1][1], d2[i - 1][2]) + cost[i][0]
    d2[i][1] = min(d2[i - 1][0], d2[i - 1][2]) + cost[i][1]
    d2[i][2] = min(d2[i - 1][0], d2[i - 1][1]) + cost[i][2]
    d3[i][0] = min(d3[i - 1][1], d3[i - 1][2]) + cost[i][0]
    d3[i][1] = min(d3[i - 1][0], d3[i - 1][2]) + cost[i][1]
    d3[i][2] = min(d3[i - 1][0], d3[i - 1][1]) + cost[i][2]
d1[N-1][0] = INF
d2[N-1][1] = INF
d3[N-1][2] = INF
print(min(min(d1[N-1]),min(d2[N-1]),min(d3[N-1])))