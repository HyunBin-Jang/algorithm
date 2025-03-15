N = int(input())
cards = list(map(int, input().split()))
mx = max(cards)
exist = [False] * 1000001
d = [0] * 1000001
for c in cards:
    exist[c] = True

for i in range(1, mx // 2 + 1):
    if exist[i]:
        j = 2
        while i * j <= mx:
            if exist[i*j]:
                d[i*j] -= 1
                d[i] += 1
            j += 1

for i in cards:
    print(d[i],"", end="")