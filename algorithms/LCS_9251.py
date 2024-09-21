str1 = input()
str2 = input()

d = [[0 for _ in range(len(str1) + 1)] for _ in range(len(str2)+ 1)]
result = 0

for i in range(1, len(str1) + 1):
    for j in range(1, len(str2) + 1):
        if str1[i - 1] == str2[j - 1]:
            d[j][i] = d[j-1][i-1] + 1
        else:
            d[j][i] = max(d[j][i-1], d[j-1][i])

print(d[len(str2)][len(str1)])