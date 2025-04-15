import sys
input = sys.stdin.readline

N = int(input())
S = []
A = [0] * (N)
for _ in range(N):
    S.append(list(map(int, input().split())))
for i in range(1, N-1):
    A[i] = (S[i-1][i] + S[i][i+1] - S[i-1][i+1]) // 2

if N == 2:
    A[0] = 1
    A[1] = 1
else:
    A[0] = S[0][1] - A[1]
    A[N-1] = S[N-1][N-2] - A[N-2]

for a in A:
    print(a,"",end="")
