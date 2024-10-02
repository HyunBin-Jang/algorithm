N = int(input())
instruction = []
for _ in range(N):
    instruction.append(list(input().split()))

stack = []
for inst in instruction:
    if len(inst) == 2:
        i = inst[0]
        n = int(inst[1])
        if i == 'push':
            stack.append(n)
    else:
        i = inst[0]
        if i == 'pop':
            if stack:
                print(stack.pop())
            else:
                print(-1)
        elif i == 'size':
            print(len(stack))
        elif i == 'empty':
            if stack:
                print(0)
            else:
                print(1)
        elif i == 'top':
            if stack:
                print(stack[len(stack) - 1])
            else:
                print(-1)