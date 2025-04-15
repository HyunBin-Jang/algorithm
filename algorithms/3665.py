from collections import deque
import sys
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    n = int(input())
    t = list(map(int, input().split()))
    t = deque(t)
    m = int(input())
    degree = [0] *(n+1)
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, input().split())
        for i in range(1, n+1):
            if t[i] == a:
                degree[a] += 1
                graph[b].append(a)
                break
            elif t[i] == b:
                degree[b] += 1
                graph[a].append(b)
                break
    q = deque([])
    q.append(t.popleft())
    result = []
    while q:
        now = q.popleft()
        if degree[now] != 0:
            
        else:
            for n in graph[now]:
                degree[n] -= 1
                if degree[n] == 0:
                    q.append(n)
                else:
                    q.append(t.popleft())
            result.append(now)
    print(result)