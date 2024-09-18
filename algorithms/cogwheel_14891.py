wheel = []
R = []
for _ in range(4):
    wheel.append(input())

K = int(input())
for _ in range(K):
    R.append(list(map(int, input().split())))

def rotate(wh, d):
    if d == 1:
        a = wh[7]
        b = wh[:-1]
        print(a + b)
        return a + b
    elif d == -1:
        a = wh[0]
        b = wh[1:7]
        print(b + a)
        return b + a

for rot in R:
    rotate(wheel[rot[0]], rot[1])
