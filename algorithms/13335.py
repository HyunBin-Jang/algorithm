from collections import deque
n, w, L = map(int, input().split())
truck = list(map(int, input().split()))
truck = deque(truck)
bridge = deque([0 for _ in range(w)])
crossed_truck = 0
next_truck = 0
result = 0
while crossed_truck < n:
    first = bridge.popleft()
    if first != 0:
        crossed_truck += 1
    if next_truck < n and sum(bridge) + truck[next_truck] <= L:
        bridge.append(truck[next_truck])
        next_truck += 1
    else:
        bridge.append(0)
    result += 1
print(result)