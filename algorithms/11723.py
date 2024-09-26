import sys
M = int(input())
S = [0] * 21
result = ''

for _ in range(M):
    inst = sys.stdin.readline().split()
    if len(inst) > 1:
        if inst[0] == "add":
            x = int(inst[1])
            if S[x] == 1:
                continue
            else:
                S[x] = 1
        elif inst[0]  == "remove":
            x = int(inst[1])
            if S[x] == 0:
                continue
            else:
                S[x] = 0
        elif inst[0]  == "check":
            x = int(inst[1])
            if S[x] == 1:
                sys.stdout.write('1' + '\n')
            else:
                sys.stdout.write('0' + '\n')
        elif inst[0]  == "toggle":
            x = int(inst[1])
            if S[x] == 1:
                S[x] = 0
            else:
                S[x] = 1
    else:
        if inst[0] == "all":
            S = [1] * 21
        elif inst[0] == "empty":
            S = [0] * 21

