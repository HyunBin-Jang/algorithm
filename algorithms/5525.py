N = int(input())
S_len = int(input())
S = input()

Pn = "I" + "OI" * N

def find_p(start):
    case = 0
    j = S.find(Pn, start)
    ioi_end = 0
    if j != -1:
        case += 1
        ioi_end = j + 2*N
        while ioi_end < S_len - 3:
            if S[ioi_end + 1] == 'O' and S[ioi_end + 2] == 'I':
                case += 1
                ioi_end += 2
            else:
                break
    if case == 0:
        return 0, S_len
    else:
        return case, ioi_end

result = 0
i = 0
while i < S_len:
    c, i = find_p(i)
    i += 1
    result += c

print(result)
