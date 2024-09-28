from sys import stdin
N = int(input())
Nums = list(map(int, stdin.readline().split()))
S_Nums = sorted(Nums)

for i in range(1, N):
    if Nums[i]