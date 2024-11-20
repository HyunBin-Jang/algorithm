S = input()
T = input()

result = 0
i = len(T) - 1
l = len(S)

while i >= l:
    if T[i] == 'A':
        T = T[:-1]
    elif T[i] == 'B':
        T = T[:-1]
        T = T[::-1]
    i -= 1

if S == T:
    result = 1
print(result)