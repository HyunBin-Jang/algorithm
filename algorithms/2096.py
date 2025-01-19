import sys
input = sys.stdin.readline
N = int(input())

before_mx = [0] * 3
d_mx = [0] * 3
before_mn = [0] * 3
d_mn = [0] * 3

for _ in range(N):
    v0, v1, v2 = (map(int, input().split()))

    d_mx[0] = max(before_mx[0], before_mx[1]) + v0
    d_mn[0] = min(before_mn[0], before_mn[1]) + v0

    d_mx[1] = max(before_mx[0], before_mx[1], before_mx[2]) + v1
    d_mn[1] = min(before_mn[0], before_mn[1], before_mn[2]) + v1

    d_mx[2] = max(before_mx[1], before_mx[2]) + v2
    d_mn[2] = min(before_mn[1], before_mn[2]) + v2

    for i in range(3):
        before_mx[i] = d_mx[i]
        before_mn[i] = d_mn[i]

print(max(d_mx), min(d_mn))