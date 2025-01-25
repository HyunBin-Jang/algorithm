from collections import deque
N, K = map(int, input().split())


INF = int(1e9)
result = 0

def bfs(n, k):
    q = deque([])
    q.append((n, 0))

    d = [INF] * (k+3)
    d[n] = 0

    while q:
        now = q.popleft()
        if d[now[0]] < now[1]:
            continue
        if 2 * now[0] <= k + 2 and d[2 * now[0]] > now[1] + 1:
            q.append((2 * now[0], now[1]+1))
            d[2 * now[0]] = now[1] + 1
        if now[0] + 1 <= k and d[now[0] + 1] > now[1] + 1:
            q.append((now[0] + 1, now[1]+1))
            d[now[0] + 1] = now[1] + 1
        if now[0] - 1 > 0 and d[now[0] - 1] > now[1] + 1:
            q.append((now[0] - 1, now[1]+1))
            d[now[0] - 1] = now[1] + 1
    return d[k]

if N >= K:
    result = N - K
else:
    result = bfs(N, K)

print(result)