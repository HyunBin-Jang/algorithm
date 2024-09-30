from sys import stdin
n = int(input())
D = []
for _ in range(n):
    D.append(int(stdin.readline().strip()))

D.sort()

def round_half_up(num):
    units = int(num * 10) % 10
    if units >= 5:
        return int(num) + 1
    else:
        return int(num)

exc = round_half_up(n * 0.15)

result = 0

for i in range(exc , n - exc):
    result += D[i]

if n == 0:
    print(0)
else:
    print(round_half_up(result / (n - 2 * exc)))