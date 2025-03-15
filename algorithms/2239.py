graph = []
empty = [[False] * 9 for _ in range(9)]
for i in range(9):
    tmp = list(map(int, list(input())))
    for j in range(9):
        if tmp[j] == 0:
            empty[i][j] = True
    graph.append(tmp)

def check(y, x):
    for i in range(9):
        if y != i and graph[i][x] == graph[y][x]:
            return False
        if x != i and graph[y][i] == graph[y][x]:
            return False
    root_x = 3 * (x // 3)
    root_y = 3 * (y // 3)
    for i in range(3):
        for j in range(3):
            if root_y + i == y and root_x + j == x:
                continue
            if graph[root_y + i][root_x + j] == graph[y][x]:
                return False
    return True

def dfs():
    for i in range(9):
        for j in range(9):
            if empty[i][j]:
                for k in range(1, 10):
                    graph[i][j] = k
                    empty[i][j] = False
                    if check(i, j):
                        if dfs():
                            break
                        else:
                            graph[i][j] = 0
                            empty[i][j] = True
                    else:
                        graph[i][j] = 0
                        empty[i][j] = True
                if empty[i][j]:
                    return False
    return True

dfs()
for i in range(9):
    for j in range(9):
        print(graph[i][j], end="")
    print()
