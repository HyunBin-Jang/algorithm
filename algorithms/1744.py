import sys

input = sys.stdin.readline
N = int(input())

negative = []
positive = []
for _ in range(N):
    n = int(input())
    if n <= 0:
        negative.append(n)
    else:
        positive.append(n)

negative.sort(reverse=True)
positive.sort()

result = 0
while negative:
    n1 = negative.pop()
    if negative:
        n2 = negative.pop()
        result += n1 * n2
    else:
        result += n1

while positive:
    p1 = positive.pop()
    if positive:
        p2 = positive.pop()
        if p2 == 1:
            result += p1 + p2
        else:
            result += p1 * p2
    else:
        result += p1

print(result)