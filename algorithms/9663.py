N = int(input())

used = [-1] * N

def queen(y):
    result = 0
    for x in range(N):
        TF = True
        for i in range(y):
            if used[i] == x or y - i == abs(x - used[i]):
                TF = False
                break
        if TF:
            if y == N - 1:
                return 1
            used[y] = x
            result += queen(y+1)
    return result

print(queen(0))