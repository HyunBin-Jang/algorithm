import sys
input = sys.stdin.readline
print = sys.stdout.write
N, M = map(int, input().split())
pokemon = {}

for i in range(1, N + 1):
    pok = input().rstrip()
    pokemon[pok] = str(i)
    pokemon[str(i)] = pok

for _ in range(M):
    inp = input().rstrip()
    print(pokemon[inp] + '\n')