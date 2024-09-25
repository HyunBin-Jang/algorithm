import sys
sys.setrecursionlimit(10**9)

N, M = map(int, input().split())
graph = []
start = []
for i in range(N):
    graph.append(input())
    for j in range(M):
        if graph[i][j] == 'I':
            start.append(j)
            start.append(i)

visited = []

def dfs(x, y):
    result = 0

    if [x, y] in visited:
        return 0
    elif x < 0 or x >= M or y < 0 or y >= N or graph[y][x] == 'X':
        return 0
    elif graph[y][x] == 'P':
        result += 1

    visited.append([x, y])
    result += dfs(x - 1, y)
    result += dfs(x + 1, y)
    result += dfs(x, y - 1)
    result += dfs(x, y + 1)
    return result

result = dfs(start[0], start[1])
if result == 0:
    print("TT")
else:
    print(result)