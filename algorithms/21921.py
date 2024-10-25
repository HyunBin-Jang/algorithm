N, X = map(int, input().split())
visit = list(map(int, input().split()))

dur = 1
sum_v = sum(visit[0 : X])
mx = sum_v
for i in range(1, N - X + 1):
    sum_v -= visit[i - 1]
    sum_v += visit[i + X - 1]
    if mx == sum_v:
        dur += 1
    elif mx < sum_v:
        mx = sum_v
        dur = 1
if mx == 0:
    print("SAD")
else:
    print(mx)
    print(dur)