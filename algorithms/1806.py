import sys
input = sys.stdin.readline
N, S = map(int, input().split())
nums = list(map(int, input().split()))

total = 0
end = -1
INF = int(1e9)
result = INF

for start in range(N):
    if start > end:
        total += nums[start]
        end += 1
    if total < S:
        while total < S and end + 1 < N:
            end += 1
            total += nums[end]
    elif total > S:
        while total - nums[end] >= S and end - 1 >= start:
            total -= nums[end]
            end -= 1
    if total >= S:
        result = min(result, end - start + 1)
    total -= nums[start]

if result == INF:
    print(0)
else:
    print(result)