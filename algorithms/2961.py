from itertools import combinations
N = int(input())
ingredient = []
for _ in range(N):
    ingredient.append(list(map(int, input().split())))

min_dif = 1000000001
for n in range(1, N + 1):
    cases = list(combinations(ingredient, n))
    for c in cases:
        sour = 1
        bitter = 0
        for i in c:
            sour *= i[0]
            bitter += i[1]
        min_dif = min(min_dif, abs(sour - bitter))
print(min_dif)