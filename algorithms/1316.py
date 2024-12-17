N = int(input())
result = 0

for _ in range(N):
    S = input()
    group = True
    for i in range(len(S)):
        K = False
        for j in range(i, len(S)):
            if S[i] == S[j] and K:
                group = False
                break
            elif S[i] != S[j]:
                K = True
    if group:
        result += 1

print(result)   