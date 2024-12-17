import sys
T = int(input())
for _ in range(T):
    applicant = []
    N = int(input())
    for _ in range(N):
        applicant.append(list(map(int, sys.stdin.readline().split())))
    applicant.sort(key=lambda x : x[0])
    k = applicant[0][1]
    applicant.sort(key=lambda x: x[1])
    result = 0
    mn = applicant[0][0]
    for i in range(k):
        if applicant[i][0] <= mn:
            result += 1
            mn = applicant[i][0]
    print(result)
