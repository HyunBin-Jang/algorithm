import heapq
INF = 1000000000
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def dijkstra(result, graph, visited):
    q = []
    heapq.heappush(q,(graph[0][0],0,0))
    result[0][0] = graph[0][0]
    visited[0][0] = True
    while q:
        dist, x, y = heapq.heappop(q)
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if 0 <= new_x < N and 0 <= new_y < N and not visited[new_x][new_y]:
                result[new_x][new_y] = min(result[new_x][new_y], dist + graph[new_x][new_y])
                visited[new_x][new_y] = True
                heapq.heappush(q,(result[new_x][new_y],new_x, new_y))
T = 1
while True:
    N = int(input())
    if N == 0:
        break
    graph = []
    result = [[INF] * N for _ in range(N)]
    visited = [[False] * N for _ in range(N)]
    for _ in range(N):
        graph.append(list(map(int, input().split())))
    bfs(result, graph, visited)
    print("Problem", str(T) + ":", result[N-1][N-1])
    T += 1