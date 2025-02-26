import sys
sys.setrecursionlimit(10**9)
N = input()
M = int(input())
broken_button = []
if M != 0:
    broken_button = list(map(int, input().split()))
button = []
for i in range(10):
    if i not in broken_button:
        button.append(i)

result = [abs(int(N) - 100)]

len_N = len(N)
N = int(N)

def bfs(num, n):
    for b in button:
        tmp = num
        tmp += b * 10**n
        if len_N-2 <= n <= len_N:
            result[0] = min(result[0], abs(N - tmp) + n + 1)
        if n < len_N:
            bfs(tmp, n + 1)
bfs(0, 0)
print(result[0])