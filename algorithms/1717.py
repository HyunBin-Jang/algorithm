import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline
n, m = map(int, input().split())


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_set(parent, x, y):
    root_x = find_parent(parent, x)
    root_y = find_parent(parent, y)
    if root_x < root_y:
        parent[root_y] = root_x
    else:
        parent[root_x] = root_y

parent = [0] * (n + 1)

for i in range(n+1):
    parent[i] = i

for _ in range(m):
    op, a, b = map(int, input().split())
    if op == 0:
        union_set(parent, a, b)

    elif op == 1:
        if find_parent(parent, a) == find_parent(parent, b):
            print("YES")
        else:
            print("NO")
