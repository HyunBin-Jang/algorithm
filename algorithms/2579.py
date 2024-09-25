N = int(input())
stairs = []
d = [0] * N
for _ in range(N):
    stairs.append(int(input()))


for i in range(N):
    if i == 0:
        d[0] = stairs[0]
    elif i == 1:
        d[1] = d[0] + stairs[1]
    elif i == 2:
        d[2] = max(stairs[0] + stairs[2], stairs[1] + stairs[2])
    else:
        d[i] = max(d[i-2] + stairs[i], d[i-3] + stairs[i-1] + stairs[i])

print(d[N - 1])