T = int(input())
N = []
M = []
d = [[0]*30 for _ in range(30)]

for _ in range(T):
    S, E = map(int, input().split())
    N.append(S)
    M.append(E)


def find_case(n, m):
    sum = 0
    if d[n][m] != 0:
        return d[n][m]
    elif n == m:
        d[n][m] = 1
        return 1
    elif n == 1:
        d[n][m] = m
        return m

    for i in range(1, m-n+2):
        sum += find_case(n-1, m-i)
    d[n][m] = sum
    return sum


for i in range(T):
    print(find_case(N[i],M[i]))


