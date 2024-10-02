from collections import deque
N = int(input())
Cards = deque([i for i in range(1, N + 1)])

for _ in range(N - 1):
    Cards.popleft()
    first = Cards[0]
    Cards.popleft()
    Cards.append(first)

print(Cards[0])