from itertools import combinations

N = int(input())
S = list(map(int, input().split()))
used = []
nums = [1,2,3,4,5,6,7,8,9]
comb = list(combinations(nums, 2))
def longest_seq(t):
    mx = 1
    j = 1
    for i in range(N - 1):
        if t[i] == t[i+1]:
            j += 1
        else:
            mx = max(mx, j)
            j = 1
    mx = max(mx, j)
    return mx


mx = 0
for c in comb:
    t = S.copy()
    for i in range(N):
        if t[i] == c[0]:
            t[i] = c[1]
    mx = max(mx, longest_seq(t))

print(mx)
