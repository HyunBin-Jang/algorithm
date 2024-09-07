from collections import deque

N = int(input())

graph = []

for _ in range(N):
    graph.append(list(map(int, input())))

complex_num = 0
hm = 0
house_num = []
start = []

def dfs(x, y):
    global hm
    if x < 0 or x >= N or y < 0 or y >= N:
        return
    elif graph[x][y] == 1:
        hm += 1
        graph[x][y] = 0
        dfs(x + 1, y)
        dfs(x - 1, y)
        dfs(x, y + 1)
        dfs(x, y - 1)



def find_start():
    check = False
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 1:
                start.append(i)
                start.append(j)
                check = True
                break
        if check:
            break
    return check


while find_start():
    complex_num += 1
    dfs(start[0], start[1])
    house_num.append(hm)
    start.clear()
    hm = 0


print(complex_num)
house_num.sort()
for i in house_num:
    print(i)

