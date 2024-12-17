exp = input()

stack_alphabet = []
stack_op = []

for e in exp:
    if e == '+' or e == '-' or e == '*' or e == '-' or e == '(' or e == ')':
        stack_op.append(e)
    else:
        stack_alphabet.append(e)
result = stack_alphabet.pop()

def
while stack_alphabet:
    op = stack_op.pop()
    if op == '*' or op == '/':
        result += op
        result = stack_alphabet.pop() + result
    elif op == '-' or op == '+':
        result += op
