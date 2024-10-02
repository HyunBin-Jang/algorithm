from sys import stdin
N = int(input())
a = list(map(int, stdin.readline().split()))
A = {}
for n in a:
    A[n] = 0
M = int(input())
B = list(map(int, stdin.readline().split()))

for b in B:
    if b in A:
        print(1)
    else:
        print(0)