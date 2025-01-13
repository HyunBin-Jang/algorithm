N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))


def pulling(graph, N):
    if N == 1:
        return graph[0][0]
    tmp_graph = []
    for i in range(N // 2):
        tmp_low = []
        for j in range(N // 2):
            tmp = []
            tmp.append(graph[2 * i][2 * j])
            tmp.append(graph[2 * i][2 * j + 1])
            tmp.append(graph[2 * i + 1][2 * j])
            tmp.append(graph[2 * i + 1][2 * j + 1])
            tmp.sort()
            tmp_low.append(tmp[2])
        tmp_graph.append(tmp_low)
    return pulling(tmp_graph, N // 2)

print(pulling(graph, N))