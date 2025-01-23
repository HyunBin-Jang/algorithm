import sys, heapq
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    k = int(input())
    Q = []
    mx_Q = []
    mn_buffer = []
    mx_buffer = []

    for _ in range(k):
        op, v = input().split()
        v = int(v)
        if op == 'I':
            heapq.heappush(Q, v)
            heapq.heappush(mx_Q, -v)
        elif v == -1 and Q:
            while mx_buffer and Q and mx_buffer[0] == Q[0]:
                heapq.heappop(Q)
                heapq.heappop(mx_buffer)
            if Q:
                heapq.heappush(mn_buffer, (-1) * heapq.heappop(Q))

        elif v == 1 and mx_Q:
            while mn_buffer and mx_Q and mn_buffer[0] == mx_Q[0]:
                heapq.heappop(mx_Q)
                heapq.heappop(mn_buffer)
            if mx_Q:
                heapq.heappush(mx_buffer, (-1) * heapq.heappop(mx_Q))

    for i in range(len(mx_Q)):
        mx_Q[i] *= -1
    result = set(Q) & set(mx_Q)
    result = list(result)
    result.sort()
    if result:
        print(result[len(result)-1], result[0])
    else:
        print("EMPTY")