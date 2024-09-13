from os import times

N = int(input())
fluids = list(map(int, input().split()))

fluids.sort()
start = 0
end = N-1

sp = 0
ep = 0
min_abs = 2000000001

while start != end:
    sum = fluids[start] + fluids[end]
    if abs(sum) < min_abs:
        min_abs = abs(sum)
        sp = start
        ep = end
    if sum > 0:
        end -= 1
    elif sum < 0:
        start += 1
    else:
        break

print(fluids[sp], fluids[ep])