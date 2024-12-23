import sys
N, H = map(int, input().split())
obstacle1 = []
obstacle2 = []
for i in range(N):
    n = int(sys.stdin.readline().rstrip())
    if i % 2 == 0:
        obstacle1.append(n)
    else:
        obstacle2.append(n)
obstacle1.sort()
obstacle2.sort()

results = []
for h in range(1, H+1):
    start = 0
    end = N // 2 - 1
    mid = 0
    result = 0
    while start <= end:
        mid = (start + end) // 2
        if obstacle1[mid] < h:
            start = mid + 1
        else:
            end = mid - 1
    if obstacle1[mid] < h:
        result += N // 2 - mid - 1
    else:
        result += N // 2 - mid

    start = 0
    end = N // 2 - 1
    while start <= end:
        mid = (start + end) // 2
        if obstacle2[mid] < H - h + 1:
            start = mid + 1
        else:
            end = mid - 1
    if obstacle2[mid] < H - h + 1:
        result += N // 2 - mid - 1
    else:
        result += N // 2 - mid
    results.append(result)

results.sort()
mn = results[0]
i = 0
while results[i] == mn:
    i += 1
print(mn, i)