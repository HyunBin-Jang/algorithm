X, Y = map(int, input().split())
Z = int((Y * 100) / X)

start = 1
end = 1000000000

result = -1

while start <= end:
    mid = (start + end) // 2
    new_Z = int((Y + mid) * 100/(X+mid))
    if new_Z != Z:
        result = mid
        end = mid - 1
    else:
        start = mid + 1
print(result)