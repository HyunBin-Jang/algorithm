T = int(input())

for _ in range(T):
    vps = input()
    c = 0
    result = True
    for s in vps:
        if s == '(':
            c += 1
        elif s == ')':
            c -= 1
        if c < 0:
            result = False
            break
    if c != 0:
        result = False

    if result:
        print("YES")
    else:
        print("NO")