import sys
sys.setrecursionlimit(10**6)
T = int(input())
Map = []

def dfs(x, y, m, n):
    if x < 0 or x >= m or y < 0 or y >= n:
        return
    elif Map[y][x] == 1:
        Map[y][x] = 0
        dfs(x - 1, y, m, n)
        dfs(x + 1, y, m, n)
        dfs(x, y - 1, m, n)
        dfs(x, y + 1, m, n)

for _ in range(T):
    M, N, K = map(int, input().split())
    Map = [[0 for _ in range(M)] for _ in range(N)]
    Cabbage = []
    for _ in range(K):
        x, y = map(int, sys.stdin.readline().split())
        Map[y][x] = 1
        Cabbage.append([y, x])
    result = 0
    for c in Cabbage:
        if Map[c[0]][c[1]] == 1:
            dfs(c[1], c[0], M, N)
            result += 1
    print(result)