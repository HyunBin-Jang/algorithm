n = int(input())

triangle = []
for _ in range(n):
    triangle.append(list(map(int, input().split())))

for i in range(1, n):
    triangle[i][0] += triangle[i - 1][0]
    for j in range(1, i):
        triangle[i][j] += max(triangle[i-1][j-1],triangle[i-1][j])
    triangle[i][i] += triangle[i - 1][i - 1]

triangle[n-1].sort(reverse=True)
print(triangle[n-1][0])