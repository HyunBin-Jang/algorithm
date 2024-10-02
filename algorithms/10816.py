N = int(input())
Sg = list(map(int, input().split()))
M = int(input())
nums = list(map(int, input().split()))
Cards = {}
for i in Sg:
    if i in Cards:
        Cards[i] += 1
    else:
        Cards[i] = 1

for n in nums:
    if n in Cards:
        print(Cards[n],'', end = "")
    else:
        print(0,'', end = "")