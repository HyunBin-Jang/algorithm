N = int(input())

d = [1] * (N + 1)

for i in range(2, N + 1):
    d[i] = i * d[i - 1]

S = str(d[N])
result = 0
for i in range(len(S) - 1, -1, -1):
    if S[i] == '0':
        result += 1
    else:
        break

print(result)