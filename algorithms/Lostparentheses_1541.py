express = input()
exp = []

number = ''

for e in express:
    if e == '+' or e == '-':
        if number != '':
            exp.append(int(number))
        exp.append(e)
        number = ''
    else:
        number += e

exp.append(int(number))

i = 0
k = 0
for i in range(len(exp)):
    if exp[i] == '-':
        k = 1
    elif k == 1 and exp[i] == '+':
        exp[i] = '-'

result_exp = ''

for e in exp:
    if isinstance(e, int):
        result_exp += str(e)
    else:
        result_exp += e
print(eval(result_exp))
