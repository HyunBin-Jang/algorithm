from sys import stdin
N, M = map(int, stdin.readline().split())
Numbers = [0] + list(map(int, stdin.readline().split()))
Section = []
for _ in range(M):
    Section.append(list(map(int, stdin.readline().split())))

for i in range(1, N + 1):
    Numbers[i] += Numbers[i- 1]

for s in Section:
    i = s[0]
    j = s[1]
    print(Numbers[j] - Numbers[i - 1])


