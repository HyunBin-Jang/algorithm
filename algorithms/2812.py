from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
nums = deque(list(input().rstrip()))

stack = []
i = 0
stack.append(int(nums.popleft()))

while K > 0 and nums:
    i = int(nums.popleft())
    mx = stack.pop()
    K -= 1
    while stack and mx < i and K > 0:
        mx = stack.pop()
        K -= 1
    if mx < i:
        stack.append(i)
    else:
        stack.append(mx)
        K += 1
        stack.append(i)

while K > 0:
    stack.pop()
    K -= 1
while nums:
    stack.append(int(nums.popleft()))

for n in stack:
    print(n,end="")