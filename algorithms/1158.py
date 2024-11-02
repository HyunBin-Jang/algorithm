N, K = map(int, input().split())
nums = [i for i in range(1, N + 1)]
result = []
next_idx = 0
for _ in range(N):
    next_idx = (next_idx + K - 1) % len(nums)
    result.append(nums.pop(next_idx))

print('<', end = "")
for i in range(N):
    print(result[i], end = "")
    if i == N-1:
        print('>', end = "")
    else:
        print(", ", end = "")