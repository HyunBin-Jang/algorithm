import sys
input = sys.stdin.readline

R, C, M = map(int, input().split())
graph = [[0] * (C+1) for _ in range(R+1)]

sharks = [[]]
living = [True] * (M+1)

for i in range(1, M+1):
    shark = list(map(int, input().split()))
    graph[shark[0]][shark[1]] = i
    sharks.append(shark)

def fishing(c):
    for i in range(1, R+1):
        if graph[i][c] != 0:
            shark_size = sharks[graph[i][c]][4]
            living[graph[i][c]] = False
            graph[i][c] = 0
            return shark_size
    return 0

dy = [0,-1, 1, 0, 0]
dx = [0, 0, 0, 1, -1]
lotate = [0, 2, 1, 4, 3]

def move_shark():
    for i in range(1, M+1):
        if living[i]:
            r, c, s, d, z = sharks[i]
            if graph[r][c] == i:
                graph[r][c] = 0
            if d == 1 or d == 2:
                cycle = 2 * (R - 1)
                move = s % cycle
                for _ in range(move):
                    r += dy[d]
                    if r == 0:
                        r = 2
                        d = lotate[d]
                    elif r == R + 1:
                        r = R - 1
                        d = lotate[d]
            else:
                cycle = 2 * (C - 1)
                move = s % cycle
                for _ in range(move):
                    c += dx[d]
                    if c == 0:
                        c = 2
                        d = lotate[d]
                    elif c == C + 1:
                        c = C - 1
                        d = lotate[d]
            if graph[r][c] != 0 and graph[r][c] < i:
                if z > sharks[graph[r][c]][4]:
                    living[graph[r][c]] = False
                    graph[r][c] = i
                    sharks[i] = [r, c, s, d, z]
                else:
                    living[i] = False
            else:
                graph[r][c] = i
                sharks[i] = [r, c, s, d, z]
result = 0
for i in range(1, C+1):
    result += fishing(i)
    move_shark()

print(result)