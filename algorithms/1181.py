N = int(input())
Strs = [[] for _ in range(51)]
for _ in range(N):
    inp = input()
    Strs[len(inp)].append(inp)

for i in range(51):
    if Strs[i]:
        S = sorted(list(set(Strs[i])))
        for s in S:
            print(s)