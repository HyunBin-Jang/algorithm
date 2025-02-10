from collections import deque
N, M = map(int, input().split())

INF = int(1e9)
d = [INF] * 101

ladders = [0] * 101
snakes = [0] * 101
graph = [0] * 101
for _ in range(N):
    start, end = map(int, input().split())
    graph[start] = 1
    ladders[start] = end
for _ in range(M):
    start, end = map(int, input().split())
    graph[start] = 2
    snakes[start] = end

def bfs():
    q = deque([])
    q.append((1, 0))
    while q:
        before = q.popleft()
        if d[before[0]] < before[1]:
            continue
        for i in range(1, 7):
            now = before[0] + i
            if now > 100:
                break
            if graph[now] == 1 and d[ladders[now]] > before[1] + 1:
                d[ladders[now]] = before[1] + 1
                q.append((ladders[now], d[ladders[now]]))
            elif graph[now] == 2 and d[snakes[now]] > before[1] + 1:
                d[snakes[now]] = before[1] + 1
                q.append((snakes[now], d[snakes[now]]))
            elif graph[now] == 0 and d[now] > before[1] + 1:
                d[now] = before[1] + 1
                q.append((now, d[now]))
bfs()
print(d[100])