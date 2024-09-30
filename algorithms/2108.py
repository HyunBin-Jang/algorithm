from sys import stdin
N = int(input())
nums = []
frequency = [0] * 8001
sumofNum = 0
for _ in range(N):
    input_num = int(stdin.readline().strip())
    nums.append(input_num)
    frequency[input_num + 4000] += 1
    sumofNum += input_num
nums.sort()
center = (N - 1) // 2
mx = 0
f_result = []
print(round(sumofNum / N))
print(nums[center])
for i in range(8001):
    mx = max(mx, frequency[i])
for i in range(8001):
    if frequency[i] == mx:
        f_result.append(i - 4000)
f_result.sort()
if len(f_result) >= 2 :
    print(f_result[1])
else:
    print(f_result[0])
print(nums[len(nums) - 1] - nums[0])