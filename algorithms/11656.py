S = input()
suffix = []
for i in range(len(S)):
    suffix.append(S[i:len(S)])
suffix.sort()
for s in suffix:
    print(s)