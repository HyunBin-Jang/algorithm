import sys, heapq
input = sys.stdin.readline
N = int(input())
lectures = []
for _ in range(N):
    lectures.append(list(map(int, input().split())))

lectures.sort()

classroom = []
heapq.heappush(classroom, 0)
num_class = 1

for lecture in lectures:
    fastest_end = heapq.heappop(classroom)
    if lecture[0] >= fastest_end:
        heapq.heappush(classroom, lecture[1])
    else:
        heapq.heappush(classroom, fastest_end)
        heapq.heappush(classroom, lecture[1])
        num_class += 1

print(num_class)
