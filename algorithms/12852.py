N = int(input())
d1 = [0]*(N+1)    # 최소값 DP테이블
d2 = [0]*(N+1)    # 어느 값에서 +1 되었는지
d2[1] = 1
for i in range(2,N+1):
    d1[i] = d1[i-1] + 1
    d2[i] = i - 1
    if i % 3 == 0:
        if d1[i//3] + 1 < d1[i]:
            d1[i] = d1[i//3] + 1
            d2[i] = i//3
    if i % 2 == 0:
        if d1[i//2] + 1 < d1[i]:
            d1[i] = d1[i//2] + 1
            d2[i] = i//2

print(d1[N])
j = N
while j != 1:
    print(j,"", end="")
    j = d2[j]
print(1)