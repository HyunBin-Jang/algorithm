i = input()

move = [[2,1], [2,-1], [-2,1], [-2,-1], [1,2], [-1,2],[1,-2],[-1,-2]]

i = [ord(i[0]) - 96, int(i[1])]

result = 0

for m in move:
    nx = i[0] + m[0]
    ny = i[1] + m[1]
    if nx > 0 and nx < 9 and ny > 0 and ny < 9:
        result = result + 1

print(result)
