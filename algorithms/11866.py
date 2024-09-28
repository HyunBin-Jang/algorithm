N, K = map(int, input().split())
l = [i for i in range(0, N + 1)]


i = K
result = []
while len(l) > 1:
    result.append(l.pop(i))
    for _ in range(K-1):
        if i > len(l) - 1:
            i = 1
        i += 1
        if i > len(l) - 1:
            i = 1

print('<', end = "")
for i in range(len(result)):
    if i == len(result) - 1:
        print(result[i], end="")
    else:
        print(result[i], end = ", ")
print('>', end = "")