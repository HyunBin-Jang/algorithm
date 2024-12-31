N, M, L = map(int, input().split())
cake = []
pieces = []

for i in range(M):
    cake.append(int(input()))

pieces.append(cake[0])
for i in range(1, M):
    pieces.append(cake[i] - cake[i-1])
pieces.append(L - cake[M - 1])

for _ in range(N):
    n = int(input())
    start = 0
    end = L
    result = 0
    while start <= end:
        mid = (start + end) // 2
        numOfPiece = 0
        total = 0
        for p in pieces:
            total += p
            if total >= mid:
                numOfPiece += 1
                total = 0
        if numOfPiece >= n + 1:
            result = mid
            start = mid + 1
        else:
            end = mid - 1
    print(result)