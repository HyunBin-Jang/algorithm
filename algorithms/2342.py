sequence = list(map(int, input().split()))
len_seq = len(sequence)
INF = int(1e9)
d = [[[INF] * 5 for _ in range(5)] for _ in range(len_seq - 1)]
d[0][sequence[0]][0] = 2
d[0][0][sequence[0]] = 2
force = [[0,2,2,2,2], [0,1,3,4,3], [0,3,1,3,4], [0,4,3,1,3],[0,3,4,3,1]]

for i in range(1, len_seq-1):
    n = sequence[i]
    for l in range(5):
        for r in range(5):
            if d[i-1][l][r] != INF:
                d[i][l][n] = min(d[i][l][n], d[i-1][l][r] + force[r][n])
                d[i][n][r] = min(d[i][n][r], d[i-1][l][r] + force[l][n])

print(min(min(d[len_seq - 2])))
