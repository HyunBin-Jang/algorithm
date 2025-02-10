N = int(input())
k = 1
while N // 3 != 1:
    N = N // 3
    k += 1
graph = [["***"], ["* *"], ["***"]]
def multiply_3(now):
    new = []
    first = []
    second = []
    third = []
    for i in range(len(now)):
        for j in range(len(now[i])):
            tmp = now[i][j] * 3
            first.append(tmp)
            third.append(tmp)
    for i in range(len(now)):
        for j in range(len(now[i])):
            tmp = now[i][j] + " " * (len(now[i][j])) + now[i][j]
            second.append(tmp)

    new.append(first)
    new.append(second)
    new.append(third)
    return new

def print_graph(g):
    for i in range(3):
        for j in range(len(g[i])):
            print(g[i][j])

for _ in range(k-1):
    graph = multiply_3(graph)

print_graph(graph)