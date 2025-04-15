import sys
input = sys.stdin.readline

n, m = map(int, input().split())
d = []
for _ in range(n):
    d.append(list(input().rstrip()))

for i in range(n):
    for j in range(m):
        d[i][j] = int(d[i][j])

for i in range(1,n):
    for j in range(1,m):
        if d[i][j] == 0:
            continue
        d[i][j] = min(d[i-1][j-1],d[i-1][j], d[i][j-1]) + 1
mx = 0
for i in range(n):
    for j in range(m):
        mx = max(mx, d[i][j])
print(mx**2)