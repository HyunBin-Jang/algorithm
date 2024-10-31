H, W = map(int, input().split())
graph = [[-1 for _ in range(W)] for _ in range(H)]
for i in range(H):
    weather = input()
    for j in range(W):
        if weather[j] == 'c':
            graph[i][j] = 0
for i in range(H):
    for j in range(W - 1, 0, -1):
        if graph[i][j] != 0:
            for k in range(j - 1, -1, -1):
                if graph[i][k] == 0:
                    graph[i][j] = j - k
                    break
for i in range(H):
    for j in range(W):
        print(graph[i][j], '', end ="")
    print()