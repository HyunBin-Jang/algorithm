import sys
input = sys.stdin.readline
N, M = map(int, input().split())
true_man = list(map(int, input().split()))

TF = [False] * (N+1)
true_party = [False] * M

for i in range(1, true_man[0]+1):
    TF[true_man[i]] = True

parties = []
for _ in range(M):
    party = list(map(int, input().split()))
    party.pop(0)
    parties.append(party)

change = True
while change:
    change = False
    for i in range(M):
        if true_party[i]:
            continue
        for p in parties[i]:
            if TF[p]:
                true_party[i] = True
                change = True
                break
        if true_party[i]:
            for p in parties[i]:
                TF[p] = True

result = 0
for i in range(M):
    if not true_party[i]:
        result += 1

print(result)