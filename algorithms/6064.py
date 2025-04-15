import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    M, N, x, y = map(int,input().split())

    # 종말 조건
    end_x = M - (min(M, N) - 1)
    end_y = N - (min(M, N) - 1)

    # 찾는 조건
    find_x = x - (min(x, y) - 1)
    find_y = y - (min(x, y) - 1)

    now_x = 1
    now_y = 1
    year = 1

    find = False

    while True:
        if now_x == find_x and now_y == find_y:
            year += (x - now_x)
            find = True
            break
        if now_x == end_x and now_y == end_y:
            break

        t = min((M - now_x), (N - now_y)) + 1
        now_x += t
        now_y += t
        if now_x > M:
            now_x = 1
        if now_y > N:
            now_y = 1
        year += t

        if now_x == 1 and now_y == 1:
            break
    if find:
        print(year)
    else:
        print(-1)