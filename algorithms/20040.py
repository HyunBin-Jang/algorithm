import sys
input = sys.stdin.readline

n, m = map(int, input().split())

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_set(parent, a, b):
    root_a = find_parent(parent, a)
    root_b = find_parent(parent, b)
    if root_a < root_b:
        parent[root_b] = root_a
    else:
        parent[root_a] = root_b

parent = [i for i in range(n)]
cycle = False
result = 0
for i in range(1, m+1):
    a, b = map(int, input().split())
    if find_parent(parent, a) == find_parent(parent, b) and not cycle:
        result = i
        cycle = True
    union_set(parent, a, b)

print(result)