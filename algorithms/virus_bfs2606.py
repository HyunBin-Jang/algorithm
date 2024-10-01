from collections import deque

n = int(input())
pair_num = int(input())
graph = [[]for _ in range(n+1)]
start = 1
visited = []

for _ in range(pair_num):
    t = list(map(int, input().split()))
    graph[t[0]].append(t[1])
    graph[t[1]].append(t[0])


def bfs():
    queue = deque([])
    queue.append(start)
    result = 0
    visited.append(start)
    while queue:
        e = queue.popleft()
        for i in graph[e]:
            if i not in visited:
                queue.append(i)
                visited.append(i)
                result += 1

    return result

print(bfs())