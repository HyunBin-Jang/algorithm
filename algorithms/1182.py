from itertools import combinations

N, S = map(int,input().split())
sequence = list(map(int, input().split()))


result = 0
for n in range(1, N + 1):
    combi = combinations(list(i for i in range(N)), n)
    for c in combi:
        total = 0
        for i in c:
            total += sequence[i]
        if total == S:
            result += 1
print(result)