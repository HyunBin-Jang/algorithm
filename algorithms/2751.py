import sys
input = sys.stdin.readline

N = int(input())
Nums = []
for _ in range(N):
    Nums.append(int(input()))

Nums = list(set(Nums))
Nums.sort()

for n in Nums:
    print(n)