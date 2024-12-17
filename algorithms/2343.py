N, M = map(int, input().split())
B = list(map(int, input().split()))

S = sum(B)
start = sum(B) // M
end = S
result = 0

def check(m):
    total = 0
    i = 0
    n = 1
    while i < N and n <= M:
        if total + B[i] > m:
            total = 0
            n += 1
            continue
        total += B[i]
        i += 1

    if total <= m and n <= M:
        return True
    else:
        return False

while start <= end:
    mid = (start + end) // 2
    if check(mid):
        result = mid
        end = mid - 1
    else:
        start = mid + 1
print(result)