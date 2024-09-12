n = int(input())

e_lines = []

d = [1] * n

for _ in range(n):
    e_lines.append(list(map(int, input().split())))
# 가장 긴 부분 수열

e_lines.sort(key=lambda a : a[0])

for i in range(n):
    for j in range(i):
        if e_lines[i][1] > e_lines[j][1]:
            d[i] = max(d[i], d[j] + 1)


print(n - max(d))