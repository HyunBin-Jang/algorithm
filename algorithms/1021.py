from collections import deque
N, M = map(int, input().split())
target = list(map(int, input().split()))
q = deque([i for i in range(1, N + 1)])

def op2():
    i = q.popleft()
    q.append(i)
def op3():
    i = q.pop()
    q.appendleft(i)

result = 0
for t in target:
    t_idx = q.index(t)
    if t_idx < len(q) / 2:
        for _ in range(t_idx):
            op2()
        result += t_idx
        q.popleft()

    else:
        for _ in range(len(q) - t_idx):
            op3()
        result += (len(q) - t_idx)
        q.popleft()

print(result)
