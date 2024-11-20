import math
A, B = map(int, input().split())

mx = int(math.sqrt(B)+ 1)
d = [True] * mx
d[0] = False
d[1] = False

for i in range(2, int(math.sqrt(mx)) + 1):
    if not d[i]:
        continue
    j = 2
    while i * j < mx:
        d[i * j] = False
        j += 1

result = 0
for i in range(mx):
    if d[i]:
        j = 2
        while i ** j <= B:
            if i ** j >= A:
                result += 1
            j += 1

print(result)
