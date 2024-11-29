from itertools import combinations
Case = []
K = []
while True:
    inp = list(map(int, input().split()))
    k = inp[0]
    if k == 0:
        break
    Case.append(inp[1:k+1])

for C in Case:
    results = list(combinations(C, 6))
    for result in results:
        for r in result:
            print(r,"",end="")
        print()
    print()
