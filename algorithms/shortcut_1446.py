import heapq

N, D = map(int, input().split())

shortcut = []
d = []
graph = []

for _ in range(N):
    sc = list(map(int, input().split()))
    if sc[1] <= D and (sc[1] - sc[0] - sc[2]) > 0:
        shortcut.append(sc)

shortcut.sort(key = lambda x : x[0])

graph.append([0, shortcut[0][0], shortcut[0][0]])
for i in range(len(shortcut)):
    graph.append(shortcut[i])
    for j in range(i + 1, len(shortcut)):
        if shortcut[i][1] < shortcut[j][0]:
            graph.append([shortcut[i][1], shortcut[j][0], shortcut[j][0] - shortcut[i][1]])

def dijkstra(start):