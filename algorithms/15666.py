from copy import deepcopy

N, M = map(int, input().split())
sequence = list(map(int, input().split()))
sequence.sort()

result = []
def back(seq, remain, n):
    if n == M:
        result.append(seq)
        return
    tmp2 = deepcopy(remain)
    for i in range(len(remain)):
        tmp1 = deepcopy(seq)
        tmp1.append(remain[i])
        back(tmp1, tmp2, n + 1)
        tmp2.pop(0)

remain = deepcopy(sequence)
for i in range(N):
    seq = [sequence[i]]
    back(seq, remain,1)
    remain.pop(0)

before = []
result.sort()
for seq in result:
    if before == seq:
        continue
    before = seq
    for i in range(M):
        print(seq[i], '', end="")
    print()