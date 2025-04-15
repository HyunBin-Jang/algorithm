from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
edges = [[] for _ in range(N+1)]
degree = [0] * (N+1)
build_t = [0] * (N+1)

for i in range(1, N+1):
    inp = list(map(int, input().split()))
    build_t[i] = inp[0]
    j = 1
    while inp[j] != -1:
        edges[inp[j]].append(i)
        degree[i] += 1
        j += 1

q = deque([])
for i in range(1, N+1):
    if degree[i] == 0:
        q.append(i)

time = [0] * (N+1)
while q:
    n = q.popleft()
    time[n] += build_t[n]
    for e in edges[n]:
        degree[e] -= 1
        time[e] = max(time[e], time[n])
        if degree[e] == 0:
            q.append(e)

for i in range(1, N+1):
    print(time[i])