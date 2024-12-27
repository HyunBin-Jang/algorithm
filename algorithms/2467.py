N = int(input())
solutions = list(map(int, input().split()))

result = 2000000001
p1 = 0
p2 = 0

for i in range(N-1) :
    n = (-1) * solutions.pop(0)
    start = 0
    end = N - i - 2
    mid = 0
    while start <= end:
        mid = (start + end) // 2
        if solutions[mid] == n:
            break
        elif solutions[mid] < n:
            start = mid + 1
        elif solutions[mid] > n:
            end = mid - 1
    if solutions[mid] < n and mid < N - i - 2:
        if abs(solutions[mid] - n) > abs(solutions[mid+1]-n):
            mid = mid + 1
    elif solutions[mid] > n and mid > 0:
        if abs(solutions[mid] - n) > abs(solutions[mid - 1]-n):
            mid = mid - 1
    if result > abs((-1) * n + solutions[mid]):
        result = abs((-1) * n + solutions[mid])
        p1 = (-1) * n
        p2 = solutions[mid]
print(p1, p2)