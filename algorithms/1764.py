from sys import stdin
N, M = map(int, input().split())
unheard = {}
#unheard = []             리스트 사용시 시간초과
noseen = []
for _ in range(N):
    unheard[stdin.readline().strip()] = 1
    #unheard.append(stdin.readline().strip())
for _ in range(M):
    noseen.append(stdin.readline().strip())
result = []
for n in noseen:
    if n in unheard:
        result.append(n)

result.sort()

print(len(result))

for r in result:
    print(r)