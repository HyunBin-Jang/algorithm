import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))

d1 = [1] * N
d2 = [0] * N

for i in range(1, N):
    for j in range(i-1, -1, -1):
        if A[i] > A[j]:
            d1[i] = max(d1[i], d1[j] + 1)

for i in range(N-1, -1, -1):
    for j in range(i+1, N):
        if A[i] > A[j]:
            d2[i] = max(d2[i], d2[j] + 1)

d = [0] * N
for i in range(N):
    d[i] = d1[i]+d2[i]

print(max(d))