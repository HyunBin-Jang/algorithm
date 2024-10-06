from collections import deque
N, M = map(int, input().split())
relation = [[] for _ in range(N + 1)]
shortest = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
for _ in range(M):
    f1, f2 = map(int, input().split())
    relation[f1].append(f2)
    relation[f2].append(f1)

def bfs():
    q = deque([])
    q.append(1)
    