from collections import deque
N = int(input())
instruction = []
for _ in range(N):
    instruction.append(list(input().split()))

q = deque([])
for inst in instruction:
    if len(inst) == 2:
        i = inst[0]
        n = int(inst[1])
        if i == 'push':
            q.append(n)
    else:
        i = inst[0]
        if i == 'pop':
            if q:
                print(q.popleft())
            else:
                print(-1)
        elif i == 'size':
            print(len(q))
        elif i == 'empty':
            if q:
                print(0)
            else:
                print(1)
        elif i == 'front':
            if q:
                print(q[0])
            else:
                print(-1)
        elif i == 'back':
            if q:
                print(q[len(q) - 1])
            else:
                print(-1)