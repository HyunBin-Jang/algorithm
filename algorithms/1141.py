N = int(input())
words = []
for _ in range(N):
    words.append(input())

result = [1] * N

words.sort(key = len)
for i in range(N):
    w = words[i]
    for j in range(i + 1, N):
        t = words[j]
        if w == t[0:len(w)]:
            result[i] = 0

print(sum(result))