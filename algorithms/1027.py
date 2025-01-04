N = int(input())
building = [0] + list(map(int, input().split()))

result = 0
for i in range(1, N+1):
    s = 0
    for j in range(1, i):
        see = True
        for k in range(j+1, i):
            h = (building[i] - building[j]) * (k - i) / (i - j) + building[i]
            if h <= building[k]:
                see = False
        if see:
            s += 1
    for j in range(i+1, N+1):
        see = True
        for k in range(i+1, j):
            h = (building[i] - building[j]) * (k - i) / (i - j) + building[i]
            if h <= building[k]:
                see = False
        if see:
            s += 1
    result = max(result, s)

print(result)