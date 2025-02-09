import sys
input = sys.stdin.readline
R, C, T = map(int, input().split())

graph = []
purifier = []
for _ in range(R):
    graph.append(list(map(int, input().split())))

for i in range(R):
    for j in range(C):
        if graph[i][j] == -1:
            purifier.append((i,j))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def spread(now_graph, new_graph):
    for i in range(R):
        for j in range(C):
            if now_graph[i][j] > 0:
                numofspread = 0
                for d in range(4):
                    new_y = i + dy[d]
                    new_x = j + dx[d]
                    if 0 <= new_y < R and 0 <= new_x < C and (new_y, new_x) not in purifier:
                        numofspread += 1
                        new_graph[new_y][new_x] += now_graph[i][j] // 5
                new_graph[i][j] += now_graph[i][j] - (now_graph[i][j] // 5) * numofspread
    return new_graph

def purify(graph):
    # upward
    next_y = purifier[0][0]
    next_x = purifier[0][1]
    while next_y > 0:
        graph[next_y][next_x] = graph[next_y - 1][next_x]
        next_y -= 1
    while next_x < C - 1:
        graph[next_y][next_x] = graph[next_y][next_x + 1]
        next_x += 1
    while next_y < purifier[0][0]:
        graph[next_y][next_x] = graph[next_y + 1][next_x]
        next_y += 1
    while next_x > 1:
        graph[next_y][next_x] = graph[next_y][next_x - 1]
        next_x -= 1
    graph[purifier[0][0]][1] = 0
    graph[purifier[0][0]][0] = -1
    # downward
    next_y = purifier[1][0]
    next_x = purifier[1][1]
    while next_y < R - 1:
        graph[next_y][next_x] = graph[next_y + 1][next_x]
        next_y += 1
    while next_x < C - 1:
        graph[next_y][next_x] = graph[next_y][next_x + 1]
        next_x += 1
    while next_y > purifier[1][0]:
        graph[next_y][next_x] = graph[next_y - 1][next_x]
        next_y -= 1
    while next_x > 1:
        graph[next_y][next_x] = graph[next_y][next_x - 1]
        next_x -= 1
    graph[purifier[1][0]][1] = 0
    graph[purifier[1][0]][0] = -1
    return graph

new_graph = [[0] * C for _ in range(R)]
for p in purifier:
    new_graph[p[0]][p[1]] = -1

now = graph
for _ in range(T):
    new_graph = [[0] * C for _ in range(R)]
    for p in purifier:
        new_graph[p[0]][p[1]] = -1
    now = purify(spread(now, new_graph))

result = 0
for i in range(R):
    result += sum(now[i])

print(result + 2)