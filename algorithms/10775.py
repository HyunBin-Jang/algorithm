import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
G = int(input())
P = int(input())


parent = [0] + [i for i in range(G)]
docking = [False] * (G+1)

def find_empty(docking, parent, x):
    if docking[x]:
        parent[x] = find_empty(docking, parent, parent[x])
    else:
        return x
    return parent[x]

result = 0
for i in range(1, P+1):
    g = int(input())
    if not docking[g]:
        docking[g] = True
        result += 1
    else:
        empty = find_empty(docking, parent, g)
        if empty == 0:
            break
        docking[empty] = True
        result += 1

print(result)