n = int(input())
words = []
d = {}

for _ in range(n):
    words.append(input())

for str in words:
    for s in str:
        if s not in d:
