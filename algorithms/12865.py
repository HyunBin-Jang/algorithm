import sys
input = sys.stdin.readline
N, K = map(int, input().split())

d = [0] * (K+1)

for _ in range(N):
    W, V = map(int, input().split())
    for i in range(K-W,-1,-1):
        d[i + W] = max(d[i+W], d[i] + V)

print(d[K])