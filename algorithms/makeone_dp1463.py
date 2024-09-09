import sys

sys.setrecursionlimit(10 ** 7)

x = int(input())
d = [0] * 1000001

def min_op(i):
    if d[i] != 0:
        return d[i]
    if i == 1:
        return 0
    if i % 6 == 0:
        d[i] = min(min_op(i // 3), min_op(i // 2), min_op(i - 1)) + 1
        return d[i]
    elif i % 3 == 0:
        d[i] = min(min_op(i//3), min_op(i-1)) + 1
        return d[i]
    elif i % 2 == 0:
        d[i] = min(min_op(i//2), min_op(i-1)) + 1
        return d[i]
    else:
        d[i] = min_op(i-1) + 1
        return d[i]

result = min_op(x)

print(result)