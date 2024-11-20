from collections import deque
N = int(input())
K = int(input())
game_map = [[0] * N for _ in range(N)]
lotation = []

for _ in range(K):
    y, x = map(int, input().split())
    game_map[y-1][x-1] = 1
L = int(input())
for _ in range(L):
    lotation.append(list(input().split()))

dy = [0, 1, 0, -1]   #동 남 서 북
dx = [1, 0, -1, 0]
snake = deque([])
snake.append([0, 0])
d = 0
time = 0

def lotate(t, old_d):
    for l in lotation:
        if int(l[0]) == t:
            if l[1] == 'D':
                return (old_d + 1) % 4
            elif l[1] == 'L':
                return (old_d - 1) % 4
    return old_d

while True:
    d = lotate(time, d)
    old_head = snake[len(snake)-1]
    new_head = [old_head[0] + dy[d], old_head[1] + dx[d]]
    if  new_head[0] >= N or new_head[0] < 0 or new_head[1] >= N or new_head[1] < 0:
        time += 1
        break
    elif [new_head[0], new_head[1]] in snake:
        time += 1
        break
    elif game_map[new_head[0]][new_head[1]] == 1:
        game_map[new_head[0]][new_head[1]] = 0
        snake.append(new_head)
        time += 1
        continue
    snake.append(new_head)
    snake.popleft()
    time += 1
print(time)