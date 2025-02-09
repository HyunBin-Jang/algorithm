from collections import deque
import sys, heapq
input = sys.stdin.readline

N, L = map(int, input().split())
A = list(map(int, input().split()))

q = deque([])
D = [0] * N
min_heap = []
min_buffer = []
INF = int(1e10)
minimum = INF

for i in range(N):
    if i >= L and q:
        left = q.popleft()
        heapq.heappush(min_buffer, left)
        if left == minimum:
            while min_buffer and min_heap and min_buffer[0] == min_heap[0]:
                heapq.heappop(min_buffer)
                heapq.heappop(min_heap)
            if min_heap:
                minimum = min_heap[0]
            else:
                minimum = INF
    now = A[i]
    q.append(now)
    heapq.heappush(min_heap, now)
    if now < minimum:
        D[i] = now
        minimum = now
    else:
        D[i] = minimum

for i in range(N):
    print(D[i],'', end = "")