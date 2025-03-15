from collections import deque
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, K = map(int, input().split())
    D = [0] + list(map(int, input().split()))

    degree = [0] * (N+1)
    d = [0] * (N+1)
    edges = [[] for _ in range(N+1)]

    for _ in range(K):
        X, Y = map(int, input().split())
        degree[Y] += 1
        edges[X].append(Y)

    W = int(input())

    q = deque([])

    for i in range(1, N+1):
        if degree[i] == 0:
            q.append(i)
            d[i] = D[i]

    while q:
        now = q.popleft()
        for n in edges[now]:
            degree[n] -= 1
            d[n] = max(d[n], d[now] + D[n])
            if degree[n] == 0:
                q.append(n)
    print(d[W])
