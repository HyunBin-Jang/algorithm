import sys
input = sys.stdin.readline
N = int(input())

meetings = []
for _ in range(N):
    meetings.append(list(map(int, input().split())))
meetings.sort(key=lambda x:(x[1], x[0]))

before = -1
result = 0
meeting = []
for i in range(N):
    now = meetings[i]
    if before <= now[0]:
        before = now[1]
        result += 1
print(result)