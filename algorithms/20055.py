N, K = map(int,input().split())
belt = list(map(int,input().split()))
robot = [False] * N

def durability_zero():
    numofzero = 0
    for d in belt:
        if d == 0:
            numofzero += 1
    return numofzero

result = 0

while durability_zero() < K:
    result += 1
    belt.insert(0,belt.pop())
    robot.pop()
    robot.insert(0,False)
    robot[N-1] = False

    for i in range(N - 2, -1, -1):
        if robot[i] and not robot[i + 1] and belt[i + 1] > 0:
            robot[i] = False
            robot[i + 1] = True
            belt[i+1] -= 1

    if belt[0] != 0:
        robot[0] = True
        belt[0] -= 1

print(result)