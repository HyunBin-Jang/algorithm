N = int(input())
Map = []

for _ in range(N):
    Map.append(list(map(int, input().split())))


def div_paper(x, y, n):
    blue = 0
    white = 0
    allblue = True
    allwhite = True
    if n == 1:
        if Map[y][x] == 1:
            return [1, 0]
        else:
            return [0, 1]
    for i in range(y, y + n):
        for j in range(x, x + n):
            if Map[i][j] == 0:
                allblue = False
            if Map[i][j] == 1:
                allwhite = False
    if allblue:
        blue += 1
        return [blue, white]
    if allwhite:
        white += 1
        return [blue, white]
    else:
        d1 = div_paper(x + n // 2, y, n // 2)
        d2 = div_paper(x, y + n // 2, n // 2)
        d3 = div_paper(x + n // 2, y + n // 2, n // 2)
        d4 = div_paper(x, y, n // 2)
        blue = d1[0] + d2[0] + d3[0] + d4[0]
        white = d1[1] + d2[1] + d3[1] + d4[1]
        return [blue, white]

result = div_paper(0, 0, N)
print(result[1])
print(result[0])