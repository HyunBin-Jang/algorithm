stack = list(input())

r = 0
result = 0
before = ''
while stack:
    s = stack.pop()
    if s == ')':
        r += 1
    elif s == '(' and before == ')':
        r -= 1
        result += r
    elif s == '(':
        r -= 1
        result += 1
    before = s
print(result)