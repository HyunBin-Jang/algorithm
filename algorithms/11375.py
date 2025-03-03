import sys
input = sys.stdin.readline

N, M = map(int, input().split())

works = [[]]
for _ in range(N):
    works.append(list(map(int, input().split())))
works.sort()

d = [0 for _ in range(M+1)]
visited = [False] * (M+1)

def dfs(n, m):
    work = works[n]
    visited[m] = True
    for i in range(1, work[0] + 1):
        if d[work[i]] == 0:
            d[work[i]] = n
            return True
        elif not visited[work[i]]:
            return dfs(d[work[i]], work[i])
    return False

for i in range(1, N+1):
    work = works[i]
    for j in range(1, work[0] + 1):
        if d[work[j]] != 0 and not visited[work[j]]:
            if dfs(d[work[j]], work[j]):
                break
        elif d[work[j]] == 0:
            d[work[j]] = i
            break

result = 0
for i in range(1, M+1):
    if d[i] != 0:
        result += 1
print(result)