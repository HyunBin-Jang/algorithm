n, k = map(int,input().split())

coins = []
d = [0] * (k+1)
coins.sort()

for _ in range(n):
    coins.append(int(input()))

def find_num(i):
    if d[i] != 0:
        return 1
    elif i == 0:
        return 1
    elif i < coins[0]:
        return 0
    cases = 0
    for j in coins:
        cases += find_num(i - j)
    d[i] = cases
    print(i, cases)
    return cases

print(find_num(k))