N = int(input())

def hansu(n):
    num = list(map(int, list(str(n))))
    if len(num) == 1:
        return True
    before = num[1] - num[0]
    for i in range(1, len(num)):
        if before != num[i] - num[i - 1]:
            return False
    return True

result = 0
for i in range(1, N+1):
    if(hansu(i)):
        result += 1
print(result)