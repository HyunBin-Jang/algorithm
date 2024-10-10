import sys
N = int(input())
Nums = list(map(int, sys.stdin.readline().split()))
S_Nums = sorted(Nums)
dict = {}

result = 0
before = S_Nums[0]
dict[S_Nums[0]] = result
for i in range(1, N):
    if S_Nums[i] != before:
        result += 1
        dict[S_Nums[i]] = result
        before = S_Nums[i]

for n in Nums:
    sys.stdout.write(str(dict[n]) + ' ')