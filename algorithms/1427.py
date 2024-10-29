N = input()
num = []
for n in N:
    num.append(int(n))
num.sort(reverse=True)
for n in num:
    print(n,end="")