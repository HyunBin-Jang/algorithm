import sys
input = sys.stdin.readline

N, M = map(int, input().split())
edges = []
for _ in range(M):
    edges.append(list(map(int, input().split())))
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

parent = [i for i in range(N+1)]
mx_cost = 0
cost = 0
for edge in edges:
    a, b, c = edge
    if find_parent(parent, a) != find_parent(parent, b):
        cost += c
        union_parent(parent, a, b)
        mx_cost = max(mx_cost, c)

print(cost - mx_cost)