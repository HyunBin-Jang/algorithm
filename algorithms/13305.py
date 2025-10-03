import sys
input = sys.stdin.readline

N = int(input())
roads = list(map(int, input().split()))
prices = list(map(int, input().split()))

now = 0

result = 0
while now < N-1:
    distance = 0
    price = prices[now]
    for i in range(now + 1, N):
        distance += roads[i-1]
        if prices[now] > prices[i] or i == N-1:
            now = i
            break
    result += distance * price
print(result)