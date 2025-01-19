from copy import deepcopy

N, M = map(int, input().split())
sequence = list(map(int, input().split()))
sequence.sort()

def back(seq, remain, n):
    if n == M:
        for i in range(n):
            print(seq[i], '', end = "")
        print()
        return
    for i in range(N - n):
        tmp1 = deepcopy(seq)
        tmp1.append(remain[i])
        tmp2 = deepcopy(remain)
        tmp2.pop(i)
        back(tmp1, tmp2, n + 1)

for i in range(N):
    seq = [sequence[i]]
    remain = deepcopy(sequence)
    remain.pop(i)
    back(seq, remain,1)