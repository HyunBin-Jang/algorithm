N = int(input())
sequence = list(map(int, input().split()))
op = list(map(int, input().split()))

M = [-1000000001, 1000000001]

def put_in(plus, minus, mul, div, result, n):
    if n >= N:
        M[0] = max(M[0], result)
        M[1] = min(M[1], result)
        return
    else:
        if plus > 0:
            tmp = result + sequence[n]
            put_in(plus - 1, minus, mul, div, tmp, n+1)

        if minus > 0:
            tmp = result - sequence[n]
            put_in(plus, minus-1, mul, div, tmp, n+1)

        if mul > 0:
            tmp = result * sequence[n]
            put_in(plus, minus, mul-1, div, tmp, n+1)

        if div > 0:
            if result < 0:
                tmp = ((-1) * result)  // sequence[n]
                tmp = (-1) * tmp
            else:
                tmp = result // sequence[n]
            put_in(plus, minus, mul, div-1, tmp, n+1)

put_in(op[0], op[1], op[2], op[3], sequence[0], 1)
print(M[0])
print(M[1])