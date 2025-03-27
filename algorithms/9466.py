import sys
input = sys.stdin.readline

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

T = int(input())
for _ in range(T):
    n = int(input())
    wanted = [0] + list(map(int, input().split()))
    parent = [i for i in range(n+1)]
    result = n

    for i in range(1, n+1):
        if wanted[i] == i:
            result -= 1
            continue
        elif find_parent(parent, i) != find_parent(parent, wanted[i]):
            union_parent(parent, i, wanted[i])
        else:
            numOfMember = 1
            w = wanted[i]
            while w != i:
                numOfMember += 1
                w = wanted[w]
            result -= numOfMember
    print(result)