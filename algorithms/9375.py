T = int(input())

for _ in range(T):
    n = int(input())
    clothes = {}
    for _ in range(n):
        name, kind = input().split()
        if kind in clothes:
            clothes[kind] += 1
        else:
            clothes[kind] = 1
    result = 1
    for k in list(clothes.keys()):
        result *= (clothes[k] + 1)

    result -= 1                 #알몸 제외
    print(result)