from collections import deque
import sys
sys.setrecursionlimit(10**6)
A, B = map(int,input().split())

def bfs():
    possible = False
    q = deque([])
    q.append([A, 0])
    while q:
        t = q.popleft()
        if t[0] == B:
            possible = True
            print(t[1] + 1)
            break
        elif t[0] > B:
            continue
        else:
            q.append([t[0] * 10 + 1, t[1] + 1])
            q.append([t[0] * 2, t[1] + 1])
    if not possible:
        print(-1)
bfs()