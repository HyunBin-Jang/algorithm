N, M = map(int, input().split())
target = []
for _ in range(N):
    target.append(list(map(int, input().split())))

x = 0
y = 0
score = 0
for _ in range(M):
    mx_d = 0
    mx_t = -1
    for i in range(len(target)):
        new_d = (x - target[i][0])**2 + (y - target[i][1])**2
        if mx_d < new_d:
            mx_d = new_d
            mx_t = i
    score += mx_d
    x = target[mx_t][0]
    y = target[mx_t][1]
    target.pop(mx_t)
    target.append(list(map(int, input().split())))
print(score)
