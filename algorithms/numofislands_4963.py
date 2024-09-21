import sys
sys.setrecursionlimit(10**6)

wh = []
maplist = []
while True:
    w, h = map(int,input().split())
    if w == 0 and h == 0:
        break
    wh.append([w, h])
    m = []
    for _ in range(h):
        m.append(list(map(int, input().split())))
    maplist.append(m)


def dfs(x, y, m, hw):
    if x < 0 or x >= hw[0] or y < 0 or y >= hw[1]:
        return
    if m[y][x] == 1:
        m[y][x] = 0
        dfs(x - 1, y - 1, m, hw)
        dfs(x - 1, y + 1, m, hw)
        dfs(x + 1, y - 1, m, hw)
        dfs(x + 1, y + 1, m, hw)
        dfs(x - 1, y, m, hw)
        dfs(x + 1, y, m, hw)
        dfs(x, y - 1, m, hw)
        dfs(x, y + 1, m, hw)

k = 0
for m in maplist:
    result = 0
    while True:
        sx, sy = 51, 51
        for i in range(wh[k][1]):
            for j in range(wh[k][0]):
                if m[i][j] == 1:
                    sy, sx = i, j
        if sx == 51 and sy == 51:
            break
        else:
            dfs(sx, sy, m, wh[k])
            result += 1
    k += 1
    print(result)