import sys
input = sys.stdin.readline

R, C = map(int, input().split())
graph = []
for _ in range(R):
    graph.append(list(input()))

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

def dfs(y, x):
    mx_path = 1
    for i in range(4):
        new_y = y + dy[i]
        new_x = x + dx[i]
        if 0 <= new_y < R and 0 <= new_x < C and not visited[ord(graph[new_y][new_x]) - 65]:
            visited[ord(graph[new_y][new_x]) - 65] = True
            mx_path = max(mx_path, dfs(new_y, new_x) + 1)
            visited[ord(graph[new_y][new_x]) - 65] = False
    return mx_path

mx = [[0] * C for _ in range(R)]
visited = [False] * 26
visited[ord(graph[0][0]) - 65] = True
print(dfs(0, 0))