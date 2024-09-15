from itertools import combinations
N, M = map(int, input().split())

lab = []
empty = []

for _ in range(N):
    lab.append(list(map(int, input().split())))

for i in range(N):
    for j in range(M):
        if lab[i][j] == 0:
            empty.append([i, j])

Combi_empty = list(combinations(empty, 3))


visited = []
def dfs (x, y):
    if map[0]
    dfs(x - 1, y)
for C in Combi_empty:
