import sys
input = sys.stdin.readline

N = int(input())
lines = []
for _ in range(N):
    lines.append(list(map(int, input().split())))
lines.sort()

inc_seq = [(lines[0][1], 0)]
before = [i for i in range(N)]
used = 1

for i in range(1, N):
    a, b = lines[i]
    if inc_seq[-1][0] < b:
        before[i] = inc_seq[-1][1]
        inc_seq.append((b, i))
        used += 1
    elif inc_seq[0][0] > b:
        inc_seq[0] = (b, i)
    else:
        start = 0
        end = used - 1
        mid = 0
        while start <= end:
            mid = (start+end)//2
            if inc_seq[mid][0] <= b:
                start = mid + 1
            else:
                end = mid - 1
        if start != 0:
            before[i] = inc_seq[start-1][1]
            inc_seq[start] = (b, i)
        else:
            inc_seq[0] = (b, i)

l = inc_seq[-1][1]
using_line = [False] * N
using_line[l] = True
while l != before[l]:
    using_line[before[l]] = True
    l = before[l]

print(N - used)
for i in range(N):
    if not using_line[i]:
        print(lines[i][0])
