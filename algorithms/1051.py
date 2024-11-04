N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(input())
mx = 1
for i in range(N-1):
    for j in range(M-1):
        t = graph[i][j]
        square_len = 0
        for k in range(j + 1, M):
            if t == graph[i][k]:
                square_len = k - j + 1
                if i + square_len - 1 < N :
                    if graph[i + square_len - 1][j] == t and graph[i + square_len - 1][k] == t:
                        mx = max(mx, square_len ** 2)

print(mx)