N, D = map(int, input().split())
graph = []
d = [i for i in range(D + 1)]
for _ in range(N):
    graph.append(list(map(int, input().split())))

graph.sort(key=lambda x:x[1])
for shortcut in graph:
    if shortcut[1] > D:
        continue
    if d[shortcut[1]] > d[shortcut[0]] + shortcut[2]:
        dif = d[shortcut[1]] - d[shortcut[0]] - shortcut[2]
        for i in range(shortcut[1], D+1):
            d[i] = d[i] - dif
print(d[D])
