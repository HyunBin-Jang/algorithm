import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
idx = [0,0,0]
mx = 0

def multiply_values(start, end):
    mul = 1
    for i in range(start, end):
        mul *= A[i]
    return mul


for i in range(1, N-2):
    idx[0] = i
    for j in range(i+1, N-1):
        idx[1] = j
        for k in range(j+1, N):
            idx[2] = k
            mx = max(mx, multiply_values(0, idx[0]) + multiply_values(idx[0], idx[1]) +
                     multiply_values(idx[1], idx[2]) + multiply_values(idx[2], N))
print(mx)