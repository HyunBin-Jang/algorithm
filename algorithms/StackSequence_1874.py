n = int(input())

stack = []
seq = []
result = []

for _ in range(n):
    seq.append(int(input()))

j = 0           # 현재 처리중인 seq index

def nextlarger(i):
    for k in range(j, n):
        if seq[k] >= i:
            print(seq[k])
            return seq[k]

i = 1
find = True

while j != n and find == True:
    l = nextlarger(i)
    while i != l:
        stack.append(i)
        result.append('+')
        i += 1
    while stack:
        if stack.pop() == seq[j]:
            result.append('-')
            j += 1
            break

print(result)