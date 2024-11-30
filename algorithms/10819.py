from itertools import permutations
N = int(input())
A = list(map(int, input().split()))

def exp(a):
    n = 0
    for i in range(N-1):
        n += abs(a[i] - a[i+1])
    return n

pmt = list(permutations(A))

result = 0
for p in pmt:
    result = max(result, exp(p))
print(result)