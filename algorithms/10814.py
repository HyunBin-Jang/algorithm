import sys
N = int(input())
Members = [[] for _ in range(201)]

for _ in range(N):
    age, name = sys.stdin.readline().split()
    Members[int(age)].append(name)

for i in range(1, 201):
    if Members[i]:
        for m in Members[i]:
            print(i, m)
