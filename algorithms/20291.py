N = int(input())
result = []
for _ in range(N):
    file = input()
    idx = file.find('.')
    ext = file[idx + 1:len(file)]
    result.append(ext)
result.sort()
e = result[0]
num = 1
for i in range(1, len(result)):
    if e == result[i]:
        num += 1
    else:
        print(e, num)
        e = result[i]
        num = 1
print(e, num)
