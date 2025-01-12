N, M = map(int, input().split())
trees = list(map(int, input().split()))
trees.sort()


def binary_search(start, end):
    result = 0
    while start <= end:
        mid = (start + end)//2
        total = 0
        for t in trees:
            if t > mid:
                total += t - mid
        if total < M:
            end = mid - 1
        else:
            result = mid
            start = mid + 1
    return result

print(binary_search(0,trees[N-1]))