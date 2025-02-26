import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
nums.sort()
k = 0
result = 0
for i in range(N):
    if nums[i] > k + 1:
        result = k + 1
        break
    k += nums[i]
if result == 0:
    result = k + 1
print(result)