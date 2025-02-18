import sys, heapq
input = sys.stdin.readline
N = int(input())

cards = []
for _ in range(N):
    heapq.heappush(cards, int(input()))

comparison = 0
result = 0
for _ in range(N-1):
    comparison += heapq.heappop(cards)
    comparison += heapq.heappop(cards)
    heapq.heappush(cards, comparison)
    result += comparison
    comparison = 0
print(result)