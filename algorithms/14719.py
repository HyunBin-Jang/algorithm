H, W = map(int, input().split())
Block = list(map(int, input().split()))

def check(idx, h):
    left = False
    right = False
    for j in range(idx):
        if Block[j] >= h:
            left = True
    for j in range(idx+1, W):
        if Block[j] >= h:
            right = True
    return left and right

result = 0
for h in range(1, H + 1):
    for i in range(W):
        if Block[i] < h:
            if check(i, h):
                result += 1

print(result)