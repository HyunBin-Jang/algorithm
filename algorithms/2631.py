import sys
input = sys.stdin.readline
N = int(input())
child = []
for _ in range(N):
    child.append(int(input()))
d = [1] * N

for i in range(1, N):
    for j in range(i):
        if child[i] > child[j]:
            d[i] = max(d[i], d[j] + 1)
print(N - max(d))