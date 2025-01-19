A, B, C = map(int, input().split())
M = []
while B >= 10:
    M.append(A ** (B % 10))
    A = A ** 10 % C
    B = B // 10

result = A ** B
for m in M:
    result *= m
result %= C
print(result)