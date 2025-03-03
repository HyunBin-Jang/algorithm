S = input()
expl = input()

p = 0
l = len(expl)
end = l - 1
stack = []


for c in S:
    if c == expl[p]:
        stack.append(c)
        if p == end:
            for _ in range(l):
                stack.pop()
            p = 0
            tmp = ""
            for _ in range(l):
                if stack:
                    tmp = stack.pop() + tmp
            for t in tmp:
                if t == expl[p]:
                    p += 1
                elif t == expl[0]:
                    p = 1
                else:
                    p = 0
                stack.append(t)
        else:
            p += 1
    elif c == expl[0]:
        stack.append(c)
        p = 1
    else:
        stack.append(c)
        p = 0
if stack:
    for s in stack:
        print(s, end="")
else:
    print("FRULA")
