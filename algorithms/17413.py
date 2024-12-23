S = input()

tag = False
result = ""
word = ""
for s in S:
    if s == '<':
        result += word[::-1]
        result += '<'
        word = ""
        tag = True
    elif s == '>':
        result += '>'
        tag = False
    elif s == ' ':
        result += word[::-1]
        result += ' '
        word = ""
    elif tag:
        result += s
    else:
        word += s
result += word[::-1]
print(result)