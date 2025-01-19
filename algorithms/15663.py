from copy import deepcopy

N, M = map(int, input().split())
sequence = list(map(int, input().split()))
sequence.sort()

result = []
def back(seq, remain, n):
    if n == M:
        result.append(seq)
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

before = []
result.sort()
for seq in result:
    if before == seq:
        continue
    before = seq
    for i in range(M):
        print(seq[i], '', end="")
    print()