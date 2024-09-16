INF = int(1e9)

# n 노드의 개수, m 간선의 개수
n, m = map(int, input().split())
# 시작 노드
start = int(input())

graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)          # 방문 여부
distance = [INF] * (n + 1)           # 최단 거리 테이블s

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])

# 방문하지 않은 노드 중에서 가장 최단 거리가 짧은 노드의 번호를 반환
def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]

    for _ in range(n - 1):
        now = get_smallest_node()
        visited[now] = True
        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost

dijkstra(start)
print(distance)