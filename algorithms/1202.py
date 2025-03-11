import sys, heapq
from heapq import heappop

input = sys.stdin.readline
N, K = map(int, input().split())

jewelry = []

for _ in range(N):
    M, V = map(int, input().split())
    heapq.heappush(jewelry,(M, V))

bags = []
for _ in range(K):
    bags.append(int(input()))
bags.sort()

result = 0
high_value = []
for i in range(K):
    w = bags[i]
    while jewelry and jewelry[0][0] <= w:
        now = heappop(jewelry)
        heapq.heappush(high_value, (-1) * now[1])
    if high_value:
        result += (-1) * heapq.heappop(high_value)

print(result)