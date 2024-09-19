Wheel = [[]]
R = []
for _ in range(4):
    Wheel.append(input())

K = int(input())
for _ in range(K):
    R.append(list(map(int, input().split())))

def rotate(wh, d):
    if d == 1:
        a = wh[7]
        b = wh[:-1]
        return a + b
    elif d == -1:
        a = wh[0]
        b = wh[1:8]
        return b + a

def ns():
    a = [1, 1, 1]

    if Wheel[1][2] == Wheel[2][6]:
        a[0] = 0
    if Wheel[2][2] == Wheel[3][6]:
        a[1] = 0
    if Wheel[3][2] == Wheel[4][6]:
        a[2] = 0
    return a

for rot in R:
    NS = ns()
    if rot[0] == 1:
        Wheel[1] = rotate(Wheel[1], rot[1])
        if NS[0] == 1:
            Wheel[2] = rotate(Wheel[2], rot[1] * (-1))
            if NS[1] == 1:
                Wheel[3] = rotate(Wheel[3], rot[1])
                if NS[2] == 1:
                    Wheel[4] = rotate(Wheel[4], rot[1] * (-1))
    elif rot[0] == 2:
        Wheel[2] = rotate(Wheel[2], rot[1])
        if NS[0] == 1:
            Wheel[1] = rotate(Wheel[1], rot[1] * (-1))
        if NS[1] == 1:
            Wheel[3] = rotate(Wheel[3], rot[1] * (-1))
            if NS[2] == 1:
                Wheel[4] = rotate(Wheel[4], rot[1])
    elif rot[0] == 3:
        Wheel[3] = rotate(Wheel[3], rot[1])
        if NS[1] == 1:
            Wheel[2] = rotate(Wheel[2], rot[1] * (-1))
            if NS[0] == 1:
                Wheel[1] = rotate(Wheel[1], rot[1])
        if NS[2] == 1:
            Wheel[4] = rotate(Wheel[4], rot[1] * (-1))
    elif rot[0] == 4:
        Wheel[4] = rotate(Wheel[4], rot[1])
        if NS[2] == 1:
            Wheel[3] = rotate(Wheel[3], rot[1] * (-1))
            if NS[1] == 1:
                Wheel[2] = rotate(Wheel[2], rot[1])
                if NS[0] == 1:
                    Wheel[1] = rotate(Wheel[1], rot[1] * (-1))


result = int(Wheel[1][0]) * 1 + int(Wheel[2][0]) * 2 + int(Wheel[3][0]) * 4 + int(Wheel[4][0]) * 8
print(result)