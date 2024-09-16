N = int(input())

lec = []

for _ in range(N):
    l = list(map(int, input().split()))
    l.append(l[1] - l[0])
    lec.append(l)

lec.sort(key = lambda x : x[2])
lec.reverse()

for i in range(N):
    for j in range(i+1, N):
        if lec[i][0] <= lec[j][0] and lec[i][1] >= lec[j][1]:
            
