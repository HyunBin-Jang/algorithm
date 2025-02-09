import math
N = int(input())

prime_n = [True for _ in range(N + 1)]
prime_n[0] = False
prime_n[1] = False
for i in range(2, int(math.sqrt(N)) + 1):
    if not prime_n[i]:
        continue
    j = 2
    while i * j <= N:
        prime_n[i * j] = False
        j += 1

nums = []
for i in range(N+1):
    if prime_n[i]:
        nums.append(i)

numofprime = len(nums)
result = 0

sum = 2
start = 0
end = 0
for i in range(numofprime):
    start = i
    if sum < N:
        while sum < N and end + 1 < numofprime:
            end += 1
            sum += nums[end]
    elif sum > N:
        while sum > N and start <= end - 1:
            sum -= nums[end]
            end -= 1
    if sum == N:
        result += 1
    sum -= nums[i]

print(result)