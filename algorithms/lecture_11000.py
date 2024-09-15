N = int(input())

lec = []
time = [0] * 1000

for _ in range(N):
    l = list(map(int, input().split()))
    for i in range(l[0], l[1]):
        time[i] += 1
    lec.append(l)
print(time)

13
23