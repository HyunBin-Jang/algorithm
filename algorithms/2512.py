N = int(input())
budget = list(map(int, input().split()))
M = int(input())

def check_budget(n):
    total = 0
    for b in budget:
        if b <= n:
            total += b
        else:
            total += n
    if total <= M:
        return True
    else:
        return False

start = 0
end = max(budget)
result = 0
while start <= end:
    mid = (start + end) // 2
    if check_budget(mid):
        result = mid
        start = mid + 1
    else:
        end = mid - 1
print(result)