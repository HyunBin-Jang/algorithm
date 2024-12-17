N, M = map(int, input().split())
basket = [i for i in range(N+1)]
for _ in range(M):
    i, j = map(int, input().split())
    tmp = basket[i]
    basket [i] = basket[j]
    basket[j] = tmp

for i in range(1, N+1):
    print(basket[i],"", end="")