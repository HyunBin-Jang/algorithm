Strs = []
while True:
    inp = input()
    if inp == '.':
        break
    Strs.append(inp)

for S in Strs:
    stack = []
    result = True
    for s in S:
        if s == '(':
            stack.append('(')
        elif s == ')':
            if not stack or stack.pop() != '(':
                result = False
                break
        elif s == '[':
            stack.append('[')
        elif s == ']':
            if not stack or stack.pop() != '[':
                result = False
                break
    if stack:
        result = False

    if result:
        print("yes")
    else:
        print("no")