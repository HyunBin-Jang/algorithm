import sys
input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    p_a = find_parent(parent, a)
    p_b = find_parent(parent, b)
    if p_a < p_b:
        parent[p_b] = p_a
    else:
        parent[p_a] = p_b

T = int(input())
for _ in range(T):
    F = int(input())
    parent = [i for i in range(F * 2)]
    numoffriends = [1] * (F * 2)
    friend = {}
    for i in range(F):
        a, b = input().split()
        a_idx, b_idx = 0, 0
        if a in friend:
            a_idx = friend[a]
        else:
            friend[a] = i * 2
            a_idx = i * 2
        if b in friend:
            b_idx = friend[b]
        else:
            friend[b] = i * 2 + 1
            b_idx = i * 2 + 1
        if find_parent(parent, a_idx) == find_parent(parent, b_idx):
            print(numoffriends[parent[a_idx]])
        else:
            if parent[a_idx] < parent[b_idx]:
                numoffriends[parent[a_idx]] += numoffriends[parent[b_idx]]
            else:
                numoffriends[parent[b_idx]] += numoffriends[parent[a_idx]]
            union_parent(parent, a_idx, b_idx)
            print(numoffriends[find_parent(parent, a_idx)])
