import sys
input = sys.stdin.readline

T = int(input())

def palindrome(word):
    n = len(word)
    for i in range(n // 2):
        if word[i] != word[n-i-1]:
            return False
    return True

for _ in range(T):
    k = int(input())
    words = []
    result = '0'
    for _ in range(k):
        words.append(input().rstrip())
    for i in range(k):
        if result != '0':
            break
        for j in range(k):
            if i == j:
                continue
            word = words[i] + words[j]
            if word[0] == word[-1] and palindrome(word):
                result = word
                break
    print(result)