import sys
input = sys.stdin.readline
print = sys.stdout.write
N = int(input())
A = list(map(int, input().split()))
d = [i for i in range(N)]

stack = [[A[0], 0]]
stack_l = 1

for i in range(1, N):
    if stack[stack_l-1][0] < A[i]:
        stack.append([A[i], i])
        d[i] = stack[stack_l-1][1]
        last = i
        stack_l += 1
    elif stack[0][0] >= A[i]:
        stack[0][0] = A[i]
        stack[0][1] = i
    else:
        start = 0
        end = stack_l-1
        mid = 0
        while start <= end:
            mid = (start+end) // 2
            if stack[mid][0] < A[i]:
                start = mid + 1
            else:
                end = mid - 1
        if start != 0:
            d[i] = stack[start-1][1]
            stack[start][0] = A[i]
            stack[start][1] = i
        else:
            stack[start][0] = A[i]
            stack[start][1] = i

result = []
i = stack[-1][1]
while d[i] != i:
    result.append(A[i])
    i = d[i]
result.append(A[i])

print(str(stack_l) + '\n')
for i in range(stack_l-1, -1, -1):
    print(str(result[i]) + " ")