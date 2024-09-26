import sys
T = int(sys.stdin.readline())
N = []
fibo_0 = [0] * 41
fibo_1 = [0] * 41
for _ in range(T):
    N.append(int(sys.stdin.readline()))

fibo_0[0] = 1
fibo_0[1] = 0

fibo_1[0] = 0
fibo_1[1] = 1
for i in range(2, 41):
    fibo_0[i] = fibo_0[i-1] + fibo_0[i-2]
    fibo_1[i] = fibo_1[i-1] + fibo_1[i-2]

for n in N:
    print(fibo_0[n], fibo_1[n])
