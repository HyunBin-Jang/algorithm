import math
T = []

while True:
    n = int(input())
    if n == 0:
        break
    T.append(n)

#Sieve of Eratosthenes
def sieveOfEratosthenes(x):
    d = [True for _ in range(x + 1)]
    d[0] = False
    d[1] = False

    for i in range(2, int(math.sqrt(x)) + 1):
        if not d[i]:
            continue
        j = 2
        while j * i <= x:
            d[j * i] = False
            j += 1
    return d.count(True)


for t in T:
    print(sieveOfEratosthenes(2*t) - sieveOfEratosthenes(t))