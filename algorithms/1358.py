W, H, X, Y, P = map(int, input().split())
player = []
for _ in range(P):
    player.append(list(map(int, input().split())))
R = H / 2
result = 0
for p in player:
    if p[0] >= X and p[0] <= X + W and p[1] >= Y and p[1] <= Y + H:
        result += 1
    elif (X - p[0])**2 + (Y + R - p[1])** 2 <= R**2 or (X + W- p[0])**2 + (Y + R - p[1])** 2 <= R**2:
        result += 1

print(result)