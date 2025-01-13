from itertools import combinations
N = int(input())

origin = []

for _ in range(N):
    origin.append(list(map(int, input().split())))

combi = list(combinations(origin, 3))
mx = 0
for polygon in combi:
    x1, y1 = polygon[0][0], polygon[0][1]
    x2, y2 = polygon[1][0], polygon[1][1]
    x3, y3 = polygon[2][0], polygon[2][1]
    mx = max(mx, 0.5 * abs((x1 * y2 + x2 * y3 + x3 * y1) - (x2 * y1 + x3 * y2 + x1 * y3)))
print(mx)