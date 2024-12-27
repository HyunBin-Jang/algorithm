import sys
N, C = map(int, input().split())
Xn = []

for _ in range(N):
    Xn.append(int(sys.stdin.readline().rstrip()))
Xn.sort()
Xn_dif = []
for i in range(1, N):
    Xn_dif.append(Xn[i] - Xn[i-1])

start = 1
end = Xn[N-1] - Xn[0]

result = 0
while start <= end:
    mid = (start + end) // 2
    remain = C - 1
    dif = 0
    for i in range(N-1):
        dif += Xn_dif[i]
        if dif >= mid:
            remain -= 1
            dif = 0
        if remain == 0:
            break
    if remain == 0:
        result = mid
        start = mid + 1
    else:
        end = mid - 1
print(result)