T = int(input())

for _ in range(T):
    inp = input()
    i = 0
    result = "YES"

    while i < len(inp):
        if i <= len(inp) - 3 and inp[i:i+3] == "100":
            i += 3
            z = 0
            while i < len(inp):
                if z == 0 and inp[i] == '1':
                    z = 1
                elif z == 1 and i + 1 <= len(inp) and inp[i: i + 3] == "100":
                    i += 3
                    z = 0
                    continue
                elif z == 1 and inp[i] == '0':
                    break
                i += 1
            if z == 0:
                result = "NO"
                break
        elif i <= len(inp) - 2 and inp[i:i+2] == "01":
            i += 2
            continue
        else:
            result = "NO"
            break
    print(result)