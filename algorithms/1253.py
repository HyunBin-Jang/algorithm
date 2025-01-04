N = int(input())
nums = list(map(int, input().split()))
nums.sort()

result = 0
for i in range(N):
    target = nums[i]
    start = 0
    end = N - 1
    while start < end:
        if nums[start] + nums[end] == target:
            if start == i:
                start += 1
            elif end == i:
                end -= 1
            else:
                result += 1
                break
        elif nums[start] + nums[end] > target:
            end -= 1
        else:
            start += 1
print(result)
