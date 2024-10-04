from sys import stdin
N, M = map(int, input().split())
pswd = {}
findpswd = []
for _ in range(N):
    s, p = stdin.readline().split()
    pswd[s] = p

for _ in range(M):
    findpswd.append(stdin.readline().rstrip())

for fp in findpswd:
    print(pswd[fp])