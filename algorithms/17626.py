import math
n = int(input())

square = [i**2 for i in range(1, int(math.sqrt(n) + 1))]

result = 4
if n in square:
    result = 1
else:
    for s in square:
        if n - s in square:
            result = 2
            break
    if result != 2:
        for s1 in square:
            for s2 in square:
                if n - s1 - s2 in square:
                    result = 3
                    break

print(result)