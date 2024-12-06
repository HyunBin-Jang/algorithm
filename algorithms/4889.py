T = 1

while True:
    case = list(input())
    if case[0] == '-':
        break
    result = 0
    stack = []

    stable = [1]
    while len(stable) != 0:
        stable = []
        for i in range(len(case) - 1):
            if case[i] == '{' and case[i+1] == '}':
                stable.append(i)
                stable.append(i+1)
        stable.sort(reverse=True)
        for s in stable:
            case.pop(s)

    i = 0
    j = 0
    for c in case:
        if c == '{':
            i += 1
        elif c == '}':
            j += 1
    if i % 2 == 0:
        result += i // 2
        result += j // 2
    else:
        result += i // 2
        result += j // 2
        result += 2
    print(str(T) + '.', result)
    T += 1