N, M = map(int, input().split())
cube = []
for _ in range(N):
    cube.append(list(map(int, input().split())))

result = 0

result += N * M * 2         # 위, 아래

side1 = 0
for i in range(N):
    before = 0
    for n in cube[i]:
        if before < n:
            side1 += (n - before)
        before = n
side2 = 0
for i in range(N):
    before = 0
    for j in range(M-1, -1, -1):
        if before < cube[i][j]:
            side2 += (cube[i][j] - before)
        before = cube[i][j]

side3 = 0
for i in range(M):
    before = 0
    for j in range(N):
        if before < cube[j][i]:
            side3 += (cube[j][i] - before)
        before = cube[j][i]

side4 = 0
for i in range(M):
    before = 0
    for j in range(N-1, -1, -1):
        if before < cube[j][i]:
            side4 += (cube[j][i] - before)
        before = cube[j][i]

result += side1 + side2 + side3 + side4
print(result)