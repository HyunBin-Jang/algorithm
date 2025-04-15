import sys
input = sys.stdin.readline
N, C = map(int,input().split())
M = int(input())
box = []

for _ in range(M):
    box.append((list(map(int, input().split()))))
box.sort(key=lambda x : x[1])

truck = [0] * (N+1)

result = 0
for i in range(M):
    a, b, c = box[i]
    able = C - max(truck[a:b])
    result += min(c, able)
    for j in range(a, b):
        truck[j] += min(c, able)
print(result)

