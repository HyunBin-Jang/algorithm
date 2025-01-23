N, K = map(int, input().split())

bottle = [0] * K

i = 0
result = 0
bottle[0] = 1
N -= 1

while True:
    if i == K and N != 0:
        result = bottle[i-1] - N
        break
    if N == 0:
        break
    if N - bottle[i] < 0:
        i += 1
        if i < K:
            N -= 1
            bottle[i] = 1
        continue
    N -= bottle[i]
    bottle[i] = bottle[i] * 2

print(result)
