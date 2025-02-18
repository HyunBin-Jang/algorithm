from collections import deque
from itertools import combinations
N = int(input())
nums = [i for i in range(1, N+1)]
populations = [0] + list(map(int, input().split()))
graph = [[]]
for _ in range(N):
    graph.append(list(map(int,input().split())))

def bfs(group, visited):
    q = deque([])
    visited[group[0]] = True
    q.append(group[0])
    while q:
        now = q.popleft()
        for i in range(1, graph[now][0] + 1):
            next = graph[now][i]
            if not visited[next] and next in group:
                visited[next] = True
                q.append(next)
INF = int(1e9)
min_result = INF
for i in range(1, N//2 + 1):
    cases = list(combinations(nums, i))
    for case in cases:
        group1 = list(case)
        group2 = []
        for n in nums:
            if n not in group1:
                group2.append(n)
        visited = [False] * (N + 1)
        bfs(group1, visited)
        bfs(group2, visited)
        able = True
        for i in range(1, N+1):
            if not visited[i]:
                able = False
        if able:
            total1 = 0
            total2 = 0
            for n in group1:
                total1 += populations[n]
            for n in group2:
                total2 += populations[n]
            min_result = min(min_result, abs(total1 - total2))

if min_result == INF:
    print(-1)
else:
    print(min_result)