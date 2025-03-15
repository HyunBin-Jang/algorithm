import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
edges = []
for _ in range(M):
    a, b, c = map(int, input().split())
    edges.append((c,a,b))
edges.sort()

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

parent = [i for i in range(N+1)]
cost = 0
for edge in edges:
    c, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        cost += c
        union_parent(parent, a, b)
print(cost)
