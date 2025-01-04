n = int(input())
nums = list(map(int, input().split()))
d = [0] * n

d[0] = nums[0]
for i in range(1, n):
    if d[i-1] < 0:
        d[i] = nums[i]
    else:
        d[i] = d[i-1] + nums[i]

print(max(d))