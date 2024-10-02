N = int(input())
Person = []

for _ in range(N):
    Person.append(list(map(int, input().split())))

for p in Person:
    result = 1
    for j in Person:
        if p[0] < j[0] and p[1] < j[1]:
            result += 1

    print(result,'',end = "")