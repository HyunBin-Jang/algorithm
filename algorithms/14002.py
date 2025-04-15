N = int(input())
A = list(map(int, input().split()))

d1 = [1] * N
d2 = [i for i in range(N)]

for i in range(N):
    for j in range(i):
        if A[i] > A[j] and d1[i] < d1[j] + 1:
            d1[i] = d1[j] + 1
            d2[i] = j
mx = 0
mx_idx = -1
for i in range(N):
    if mx < d1[i]:
        mx = d1[i]
        mx_idx = i

result = []
while d2[mx_idx] != mx_idx:
    result.append(A[mx_idx])
    mx_idx = d2[mx_idx]
result.append(A[mx_idx])

print(mx)
for i in range(mx-1, -1, -1):
    print(result[i],"",end="")