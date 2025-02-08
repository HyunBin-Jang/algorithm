import math
N = int(input())
k = int(input())

def lower_num(N, x):
    total = 0
    root_x = int(math.sqrt(x))
    for i in range(1, root_x + 1):
        total += (i - 1) * 2 + 1
    for i in range(root_x+1, min(N+1, x+1)):
        total += (x // i) * 2
    return total

start = 0
end = N * N

result = 0
while start <= end:
    mid = (start + end) // 2

    if lower_num(N, mid) >= k:
        result = mid
        end = mid - 1
    else:
        start = mid + 1
print(result)