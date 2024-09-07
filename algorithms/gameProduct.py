N, M = map(int, input().split())
y, x, d = map(int, input().split())

Map = []
result = 1

move = [[-1,0],[0,1],[1,0],[0,-1]]

for _ in range(N):
    l = list(map(int, input().split()))
    Map.append(l)


Map[y][x] = 2
count = 0         # 회전 횟수

while True:
    if count == 4:
        ny = y + move[(d+2)%4][0]             # 뒤로 이동
        nx = x + move[(d+2)%4][1]
        if nx < 0 or nx > M - 1 or ny < 0 or ny > N - 1 or Map[ny][nx] == 1:      #뒤로 갈 수 없으면
            break
        else:
            x = nx
            y = ny
            count = 0
            continue

    d = (d+3)%4                   # 반시계 회전
    ny = y + move[d][0]
    nx = x + move[d][1]


    if nx < 0 or nx > M - 1 or ny < 0 or ny > N - 1 or Map[ny][nx] == 1 or Map[ny][nx] == 2:    # 갈 수 없는 곳인지 확인
        count = count + 1
        continue

    else:
        x = nx
        y = ny
        result = result + 1
        Map[y][x] = 2
        count = 0

print(Map)
print(result)

