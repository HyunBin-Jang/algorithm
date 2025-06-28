import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n = int(input())
tree = [[] for _ in range(n+1)]

for _ in range(n-1):
    p, c, v = map(int, input().split())
    tree[p].append([c, v])
    tree[c].append([p, v])

def find_far_node(node_num, value, visited):
    mx = value
    idx = node_num
    for node in tree[node_num]:
        if not visited[node[0]]:
            visited[node[0]] = True
            v, i = find_far_node(node[0], value + node[1], visited)
            if mx < v:
                mx = v
                idx = i
    return mx, idx

visited = [False] * (n+1)
visited[1] = True
d, far_node = find_far_node(1, 0, visited)
visited = [False] * (n+1)
visited[far_node] = True
mx_result, another_node = find_far_node(far_node, 0, visited)
print(mx_result)
