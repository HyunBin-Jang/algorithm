from itertools import combinations
N = int(input())
M = N // 2
graph = []
people = [i for i in range(N)]
for _ in range(N):
    graph.append(list(map(int, input().split())))

case = list(combinations(people, M))

mn = 10**7
for c in case:
    team1 = c
    team2 = list(set(people) - set(c))

    ability1 = 0
    ability2 = 0

    for i in team1:
        for j in team1:
            ability1 += graph[i][j]
    for i in team2:
        for j in team2:
            ability2 += graph[i][j]
    mn = min(mn, abs(ability1 - ability2))

print(mn)