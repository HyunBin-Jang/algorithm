T = int(input())
for _ in range(T):
    N = int(input())
    price = list(map(int, input().split()))
    margin = [0] * N
    mx = 0
    for i in range(N-1, -1, -1):
        if mx > price[i]:
            margin[i] = mx - price[i]
        mx = max(mx, price[i])
    print(sum(margin))