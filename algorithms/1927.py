import sys
import heapq
input = sys.stdin.readline
print = sys.stdout.write

N = int(input())
instruction = []
heap = []
for _ in range(N):
    instruction.append(int(input().rstrip()))

for i in instruction:
    if i == 0:
        if not heap:
            print('0' + '\n')
        else:
            print(str(heapq.heappop(heap)) + '\n')
    else:
        heapq.heappush(heap, i)