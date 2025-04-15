str1 = input()
str2 = input()
d = [[""] * (len(str2)+1) for _ in range(len(str1)+1)]

for i in range(1, len(str1)+1):
    for j in range(1,len(str2)+1):
        if str1[i-1] == str2[j-1]:
            d[i][j] += (d[i-1][j-1] + str1[i-1])
        else:
            if len(d[i-1][j]) > len(d[i][j-1]):
                d[i][j] += d[i-1][j]
            else:
                d[i][j] += d[i][j-1]
if len(d[len(str1)][len(str2)]) != 0:
    print(len(d[len(str1)][len(str2)]))
    print(d[len(str1)][len(str2)])
else:
    print(0)