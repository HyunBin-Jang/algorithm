exp = input()

stack_alphabet = []
stack_op = []

for e in exp:
    if e == '+' or e == '-' or e == '*' or e == '/' or e == '(' or e == ')':
        stack_op.append(e)
    else:
        stack_alphabet.append(e)
result_stack = []
result = stack_alphabet.pop()

parenthesis = 0
while stack_op:
    op = stack_op.pop()
    if op == '*' or op == '/':
        result += op
        result = stack_alphabet.pop() + result
    elif op == '-' or op == '+':
        result += op
        if parenthesis == 0:
            result_stack.append(result)
            result = stack_alphabet.pop()
        else:
            result = stack_alphabet.pop() + result
    elif op == '(':
        parenthesis -= 1
    elif op == ')':
        parenthesis += 1
while result_stack:
    result += result_stack.pop()
print(result)