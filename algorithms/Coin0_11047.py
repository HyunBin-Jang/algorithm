N, K = map(int, input().split())
A = []
result = 0

for _ in range(N):
    A.append(int(input()))
A.reverse()

while K > 0:
    for i in range(N):
        if K == A[i]:
            K -= A[i]
            result += 1
            break
        elif K > A[i]:
            result += K // A[i]
            K = K % A[i]
            break

print(result)
