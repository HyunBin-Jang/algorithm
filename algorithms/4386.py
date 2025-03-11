import sys, math
input = sys.stdin.readline

n = int(input())

edges = []
point = []

for _ in range(n):
    point.append(list(map(float, input().split())))
for i in range(n):
    for j in range(i+1, n):
        p1 = point[i]
        p2 = point[j]
        d = math.sqrt((p1[0]-p2[0])**2 + (p1[1] - p2[1])**2)
        edges.append((i, j, d))
edges.sort(key=lambda x : x[2])

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

parent = [i for i in range(n+1)]

cost = 0
for edge in edges:
    a, b, c = edge
    if find_parent(parent, a) != find_parent(parent, b):
        cost += c
        union_parent(parent, a, b)

print(cost)