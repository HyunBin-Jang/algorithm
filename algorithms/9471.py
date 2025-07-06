import sys
input = sys.stdin.readline
P = int(input())

for _ in range(P):
    N, M = map(int, input().split())
    result = 0
    if M == 2:
        result = 3
    else:
        before = 1
        now = 1
        i = 2
        while True:
            tmp = now + before
            before = now
            now = tmp % M
            i += 1
            if now == 1 and before == 1:
                result = i - 2
                break
    print(N, result)