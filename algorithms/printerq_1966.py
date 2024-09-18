from collections import deque
Case = int(input())

NM = []
queue = []

for _ in range(Case):
    NM.append(list(map(int, input().split())))
    queue.append(deque(list(map(int, input().split()))))



def printer(N, M, deq):
    result = 0
    while deq:
        t = deq.popleft()
        if M == 0 and not deq:
            result = N
            print(result)
            return
        elif M == 0:
            if t < max(deq):
                deq.append(t)
                M += (len(deq) - 1)
                continue
            else:
                result = N - len(deq)
                print(result)
                return
        elif not deq:
            break
        elif t < max(deq):
            deq.append(t)
            M -= 1
            continue
        M -= 1


for i in range(Case):
    printer(NM[i][0], NM[i][1], queue[i])