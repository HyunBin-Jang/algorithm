import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

V, E = map(int, input().split())
edges = []
for _ in range(E):
    edges.append(list(map(int, input().split())))
edges.sort(key = lambda x : x[2])

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    parent_a = find_parent(parent, a)
    parent_b = find_parent(parent, b)

    if parent_a < parent_b:
        parent[parent_b] = parent_a
    else:
        parent[parent_a] = parent_b

parent = [i for i in range(V+1)]
cost = 0

for edge in edges:
    a, b, c = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        cost += c
print(cost)