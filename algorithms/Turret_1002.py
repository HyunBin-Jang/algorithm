import math
T = int(input())

case = []

for _ in range(T):
    case.append(list(map(int, input().split())))


def findloc(c):
    x1, y1, r1, x2, y2, r2 = c[0], c[1], c[2], c[3], c[4],c[5]
    r3 = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

    if r3 == 0 and r1 == r2:
        return -1
    elif r1 + r2 < r3 or r2 > r1 + r3 or r1 > r2 + r3:
        return 0
    elif r1 + r3 == r2 or r2 + r3 == r1 or r1 + r2 == r3:
        return 1
    else:
        return 2

for c in case:
    print(findloc(c))