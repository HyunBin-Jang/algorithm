n = int(input())
words = []
d = [[] for _ in range(9)]
alphabet = []
made_num = []

for _ in range(n):
    words.append(input())


for digit in words:
    for i in range(len(digit)):
        d[len(digit) - i].append(digit[i])
        if digit[i] not in alphabet:
            alphabet.append(digit[i])

for alb in alphabet:
    num = 0
    for i in range(9):
        num += int(d[i].count(alb) * (10 ** (i - 1)))

    made_num.append(num)

made_num.sort(reverse = True)

result = 0

for i in range(len(made_num)):
    result += made_num[i] * (9 - i)

print(result)