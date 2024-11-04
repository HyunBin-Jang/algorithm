R, C = map(int, input().split())
puzzle = []
for _ in range(R):
    puzzle.append(input())
words = []
for i in range(R):
    word = ""
    for j in range(C):
        if puzzle[i][j] == '#':
            if len(word) >= 2:
                words.append(word)
            word = ""
        else:
            word += puzzle[i][j]
    if len(word) >= 2:
        words.append(word)
for j in range(C):
    word = ""
    for i in range(R):
        if puzzle[i][j] == '#':
            if len(word) >= 2:
                words.append(word)
            word = ""
        else:
            word += puzzle[i][j]
    if len(word) >= 2:
        words.append(word)
words.sort()
print(words[0])