N = int(input())

result = []
for i in range(666, 2700000):
    if "666" in str(i):
        result.append(i)

result.sort()
print(result[N - 1])