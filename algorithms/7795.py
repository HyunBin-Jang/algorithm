import sys
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    B.sort()
    result = 0
    for i in range(N):
        target = A[i]
        start = 0
        end = M-1
        mid = 0
        while start <= end:
            mid = (start + end) // 2
            if B[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        if B[mid] < target:
            result += mid + 1
        else:
            result += mid
    print(result)