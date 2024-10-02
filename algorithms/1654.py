from sys import stdin
K, N = map(int, input().split())
lan = []
l_sum = 0
for _ in range(K):
    r = int(stdin.readline().rstrip())
    l_sum += r
    lan.append(r)

ceil = l_sum // N + 1
floor = 1
# 1 ~ ceil
while floor <= ceil:
    mid = (floor + ceil) // 2
    result = 0
    for l in lan:
        result += l // mid

    if result >= N:
        floor = mid + 1
    else:
        ceil = mid - 1
print(ceil)