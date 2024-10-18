T = int(input())
for _ in range(T):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    planet = []
    for _ in range(n):
        planet.append(list(map(int, input().split())))
    result = 0
    start_in = []
    dest_in = []
    for i in range(n):
        if (planet[i][0] - x1)**2 + (planet[i][1] - y1)**2 < (planet[i][2] ** 2) :
            start_in.append(i)
        if (planet[i][0] - x2)**2 + (planet[i][1] - y2)**2 < (planet[i][2] ** 2) :
            dest_in.append(i)
    for i in start_in:
        if (planet[i][0] - x2)**2 + (planet[i][1] - y2)**2 > (planet[i][2] ** 2) :
            result += 1
    for i in dest_in:
        if (planet[i][0] - x1)**2 + (planet[i][1] - y1)**2 > (planet[i][2] ** 2) :
            result += 1
    print(result)