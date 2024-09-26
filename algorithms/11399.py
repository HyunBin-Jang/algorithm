N = int(input())
T =  list(map(int, input().split()))

T.sort()
for i in range(1, N):
    T[i] += T[i - 1]

result = sum(T[i] for i in range(N))
print(result)