n = int(input())

stack = []
seq = []
result = []
available = True

for _ in range(n):
    seq.append(int(input()))

j = 1           # stack에 넣을 다음 값

# 수열 첫번째 값 처리
for i in range(1, seq[0] + 1):
    stack.append(i)
    result.append('+')
    j += 1

stack.pop()
result.append('-')

# 수열 나머지 값 처리
for i in range(1, n):
    if seq[i] < seq[i - 1]:
        if seq[i] not in stack:
            available = False
            break
        k = 0
        while k != seq[i]:
            k = stack.pop()
            result.append('-')
    else:
        if seq[i] < j:
            available = False
            break
        for k in range(j, seq[i] + 1):
            stack.append(k)
            result.append('+')
            j += 1
        stack.pop()
        result.append('-')

if not available:
    print("NO")
else:
    for r in result:
        print(r)