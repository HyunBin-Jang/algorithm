n = int(input())
fibo = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597]
used = {}

def bfs(x):
    if x <= 17:
        return fibo[x]
    elif x in used:
        return used[x]
    elif x % 2 == 1:
        result = (bfs(x // 2 + 1) ** 2 + bfs(x // 2) ** 2) % 1000000007
        used[x] = result
        return result
    else:
        result = (bfs(x // 2) ** 2 + 2 * bfs(x // 2) * bfs(x // 2 - 1)) % 1000000007
        used[x] = result
        return result

print(bfs(n))