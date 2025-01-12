import sys
N = int(input())
stack = []
result = 0
for _ in range(N):
    work = list(map(int,sys.stdin.readline().split()))
    if work[0] == 1:
        if work[2] == 1 :
            result += work[1]
        else:
            stack.append([work[2] - 1, work[1]])
    else:
        if stack:
            assignment = stack.pop()
            assignment[0] -= 1
            if assignment[0] == 0:
                result += assignment[1]
            else:
                stack.append(assignment)
print(result)