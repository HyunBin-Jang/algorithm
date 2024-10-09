import sys
import heapq
input = sys.stdin.readline
print = sys.stdout.write

N = int(input())
instruction = []
heap1 = []       #positive
heap2 = []       #negative
for _ in range(N) :
    instruction.append(int(input().rstrip()))

for i in instruction:
    if i == 0:
        if not heap1 and not heap2:
            print('0' + '\n')
        elif not heap1:
            print(str(-1 * heapq.heappop(heap2)) + '\n')
        elif not heap2:
            print(str(heapq.heappop(heap1)) + '\n')
        else:
            p = heapq.heappop(heap1)
            n = heapq.heappop(heap2)
            if p < n:
                print(str(p) + '\n')
                heapq.heappush(heap2, n)
            else:
                print(str(-1 * n) + '\n')
                heapq.heappush(heap1, p)
    else:
        if i > 0:
            heapq.heappush(heap1, i)
        elif i < 0:
            heapq.heappush(heap2, -1 * i)