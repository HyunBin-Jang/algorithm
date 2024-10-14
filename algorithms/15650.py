from itertools import combinations
N, M = map(int, input().split())
nums = [i for i in range(1, N + 1)]

combi = list(combinations(nums, M))

for c in combi:
    for n in c:
        print(n,'', end="")
    print()