str1 = input()
str2 = input()

firsted = []
result = 0

for l in range(len(str1)):
    if str1[l] in firsted:
        continue
    else:
        firsted.append(str1[l])
    lcs = ''
    k = 0
    for i in range(l, len(str1)):
        for j in range(k, len(str2)):
            if str1[i] == str2[j]:
                lcs += str1[i]
                k = j + 1
    print(lcs)
    result = max(result, len(lcs))

print(result)