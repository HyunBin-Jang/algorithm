T = int(input())
dy = [1, 0, -1, 0]      # 북, 동, 남, 서
dx = [0, 1, 0 , -1]
for _ in range(T):
    inst = input()
    visited = [[0, 0]]
    present = [0, 0]
    n = 0   # 방향
    for i in inst:
        if i == 'F':
            visited.append([present[0] + dx[n], present[1] + dy[n]])
            present[0] += dx[n]
            present[1] += dy[n]
        elif i == 'B':
            visited.append([present[0] - dx[n], present[1] - dy[n]])
            present[0] -= dx[n]
            present[1] -= dy[n]
        elif i == 'L':
            n = (n + 3) % 4
        elif i == 'R':
            n = (n + 1) % 4
    visited.sort()
    width = visited[len(visited) - 1][0] - visited[0][0]
    visited.sort(key = lambda x : x[1])
    height = visited[len(visited) - 1][1] - visited[0][1]
    print(width * height)