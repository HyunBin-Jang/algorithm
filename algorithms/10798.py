S = []
for _ in range(5):
    S.append(list(input()))

for i in range(15):
    for s in S:
        if len(s) >= i + 1:
            print(s[i], end="")
                