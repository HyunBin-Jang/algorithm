import sys
input = sys.stdin.readline

N = int(input())
planet = []
edges = []
for i in range(N):
    planet.append([i] + list(map(int, input().split())))

planet.sort(key=lambda x:x[1])
for i in range(1, N):
    edges.append((abs(planet[i][1] - planet[i-1][1]), planet[i][0], planet[i-1][0]))
planet.sort(key=lambda x:x[2])
for i in range(1, N):
    edges.append((abs(planet[i][2] - planet[i-1][2]), planet[i][0], planet[i-1][0]))
planet.sort(key=lambda x:x[3])
for i in range(1, N):
    edges.append((abs(planet[i][3] - planet[i-1][3]), planet[i][0], planet[i-1][0]))

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


parent = [i for i in range(N)]
def union_parent(parent, a, b):
    parent_a = find_parent(parent, a)
    parent_b = find_parent(parent, b)

    if parent_a < parent_b:
        parent[parent_b] = parent_a
    else:
        parent[parent_a] = parent_b

edges.sort()
cost = 0
for edge in edges:
    c, i, j = edge
    if find_parent(parent, i) != find_parent(parent, j):
        union_parent(parent, i, j)
        cost += c
print(cost)