import sys, heapq
input = sys.stdin.readline

n = int(input())
m = int(input())

INF = int(1e9)
graph = [[] for _ in range(n+1)]
d = [INF] * (n + 1)

for _ in range(m):
    s, e, c = map(int, input().split())
    graph[s].append((e,c))

start, end = map(int, input().split())

d[start] = 0
path = [0] * (n+1)

q = []
heapq.heappush(q, (start, 0, 0))

while q:
    now = heapq.heappop(q)
    if d[now[0]] < now[1]:
        continue
    path[now[0]] = now[2]
    for e in graph[now[0]]:
        if d[e[0]] > now[1] + e[1]:
            d[e[0]] = now[1] + e[1]
            heapq.heappush(q, (e[0], d[e[0]], now[0]))

end_path = []
i = end
while i != 0:
    end_path.append(i)
    i = path[i]
end_path.reverse()
print(d[end])
print(len(end_path))
for p in end_path:
    print(p, '', end = "")