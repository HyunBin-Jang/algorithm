T = int(input())
for _ in range(T):
    n = int(input())
    sticker = []
    sticker.append(list(map(int,input().split())))
    sticker.append(list(map(int,input().split())))
    d = [[0] * n, [0] * n]
    d[0][0] = sticker[0][0]
    d[1][0] = sticker[1][0]

    if n >= 2:
        d[0][1] = d[1][0] + sticker[0][1]
        d[1][1] = d[0][0] + sticker[1][1]

    for i in range(2, n):
        d[0][i] = max(d[1][i-1], d[1][i-2]) + sticker[0][i]
        d[1][i] = max(d[0][i-1], d[0][i-2]) + sticker[1][i]

    print(max(d[0][n-1], d[1][n-1]))
