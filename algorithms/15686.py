from itertools import combinations
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
houses = []
chicken = []

for i in range(N):
    low = list(map(int, input().split()))
    for j in range(N):
        if low[j] == 1:
            houses.append((i, j))
        if low[j] == 2:
            chicken.append((i, j))
cases = list(combinations(chicken, M))

INF = int(1e9)
min_distance = INF

for case in cases:
    city_distance = 0
    for house in houses:
        distance = INF
        for c in case:
            distance = min(distance, abs(house[0] - c[0]) + abs(house[1] - c[1]))
        city_distance += distance
    min_distance = min(min_distance, city_distance)
print(min_distance)