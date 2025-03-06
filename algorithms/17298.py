N = int(input())
A = list(map(int, input().split()))

stack = []
result = [-1] * N
for i in range(N - 1):
    if A[i] >= A[i+1]:
        stack.append(i)
    else:
        result[i] = A[i+1]
        while stack:
            top = stack.pop()
            if A[top] < A[i+1]:
                result[top] = A[i+1]
            else:
                stack.append(top)
                break

for n in result:
    print(n,"",end="")
