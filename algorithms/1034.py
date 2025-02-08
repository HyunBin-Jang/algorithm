N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(input())
K = int(input())

result = 0
for i in range(N):
    tmp = graph[i]
    zero_num = 0
    for s in tmp:
        if s == '0':
            zero_num += 1
    if zero_num <= K and zero_num % 2 == K % 2:
        total = 0
        for j in range(N):
            if tmp == graph[j]:
                total += 1
        result = max(result, total)

print(result)