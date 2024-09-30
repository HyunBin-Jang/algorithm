from sys import stdin
K = int(input())
nums = []


for i in range(K):
    n = int(stdin.readline().strip())
    if n == 0:
        nums.pop()
    else:
        nums.append(n)

result = 0
for r in nums:
    result += r
print(result)