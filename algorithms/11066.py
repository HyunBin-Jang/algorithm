import sys
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    K = int(input())
    files = list(map(int, input().split()))
    d = [0] * (K-1)
    for i in range(K-1):
        d[i] = files[i] + files[i+1]
    for i in range(K-1):
        d[i] 