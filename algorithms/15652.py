from itertools import combinations_with_replacement
N, M = map(int, input().split())
result = list(combinations_with_replacement([i for i in range(1, N + 1)], M))

for r in result:
    for i in r:
        print(i,'',end='')
    print()