N, M = map(int, input().split())
DNA = []
HD = {'A': 0, 'T': 0, 'G': 0, 'C': 0}
for _ in range(N):
    inp = input()
    DNA.append(inp)
result = ""
min_HD = 0
for i in range(M):
    for c in "ACGT":
        HD[c] = 0
    for D in DNA:
        HD[D[i]] += 1
    tmp = list(HD.values())
    tmp.sort(reverse=True)
    mx = tmp[0]
    for c in "ACGT":
        if HD[c] == mx:
            result += c
            break
    min_HD += N - mx

print(result)
print(min_HD)