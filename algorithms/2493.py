import sys, heapq
input = sys.stdin.readline
N = int(input())
top = [0] + list(map(int, input().split()))

d = [0] * (N+1)
q = []

for i in range(N, 0, -1):
    while q:
        tmp = heapq.heappop(q)
        if tmp[0] <= top[i]:
            d[tmp[1]] = i
        else:
            heapq.heappush(q, tmp)
            break
    heapq.heappush(q, (top[i], i))

for i in range(1, N+1):
    print(d[i],'', end="")