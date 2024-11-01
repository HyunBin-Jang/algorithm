graph = []
call = []
bingo = [[0 for _ in range(5)] for _ in range(5)]
for _ in range(5):
    graph.append(list(map(int, input().split())))
for _ in range(5):
    for i in list(map(int, input().split())):
        call.append(i)

def checkbingo():
    numofbingo = 0
    for i in range(5):
        bg1 = True
        bg2 = True
        for c in bingo[i]:
            if c == 0:
                bg1 = False
                break
        for j in range(5):
            if bingo[j][i] == 0:
                bg2 = False
                break
        if bg1:
            numofbingo += 1
        if bg2:
            numofbingo += 1
    bg3 = True
    bg4 = True
    for i in range(5):
        if bingo[i][i] == 0:
            bg3 = False
        if bingo[4 - i][i] == 0:
            bg4 = False
    if bg3:
        numofbingo += 1
    if bg4:
        numofbingo += 1
    if numofbingo >= 3:
        return True
    else:
        return False
result = 0
for c in call:
    for i in range(5):
        for j in range(5):
            if graph[i][j] == c:
                bingo[i][j] = 1
                break
    result += 1
    if checkbingo():
        print(result)
        break