import sys
N = int(input())
components = list(map(int, sys.stdin.readline().rstrip().split()))
M = int(input())
request = list(map(int, sys.stdin.readline().rstrip().split()))
request.sort()
found = [False] * M

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            found[mid] = True
            return
        elif array[mid] > target:
            end = mid-1
        elif array[mid] < target:
            start = mid+1
    return

for c in components:
    binary_search(request, c, 0, M-1)

for i in range(M):
    if found[i]:
        sys.stdout.write("yes ")
    else:
        sys.stdout.write("no ")