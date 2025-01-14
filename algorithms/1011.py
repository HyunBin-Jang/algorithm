T = int(input())

for _ in range(T):
    x, y = map(int, input().split())
    result = y - x
    start = 0
    end = y - x
    d = y - x
    while start <= end:
        mid = (start + end) // 2
        remain = d - mid * (mid + 1)
        if remain == 0:
            result = 2 * mid
            break
        elif 0 < remain <= mid + 1:
            result = 2 * mid + 1
            break
        elif 0 < remain < 2 * (mid + 1):
            result = 2 * mid + 2
            break
        elif remain < 0:
            end = mid - 1
        else:
            start = mid + 1
    print(result)
