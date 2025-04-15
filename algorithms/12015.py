import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

stack = [A[0]]
stack_l = 1
for i in range(1, N):
    if stack[stack_l-1] < A[i]:
        stack.append(A[i])
        stack_l += 1
    elif stack[0] >= A[i]:
        stack[0] = A[i]
    else:
        start = 0
        end = stack_l-1
        mid = 0
        while start <= end:
            mid = (start+end) // 2
            if stack[mid] < A[i]:
                start = mid + 1
            else:
                end = mid - 1
        stack[start] = A[i]
print(stack_l)