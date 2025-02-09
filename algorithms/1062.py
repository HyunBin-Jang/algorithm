from copy import deepcopy
from itertools import combinations
import sys
input = sys.stdin.readline
N, K = map(int, input().split())
alphabet = [False] * 26
alphabet[ord('a') - 97] = True
alphabet[ord('n') - 97] = True
alphabet[ord('t') - 97] = True
alphabet[ord('i') - 97] = True
alphabet[ord('c') - 97] = True

others = []
words = []
for _ in range(N):
    word = input().rstrip()
    for w in word:
        if not alphabet[ord(w) - 97] and w not in others:
            others.append(w)
    words.append(word)


result = 0
if K < 5:
    print(result)
else:
    if len(others) < (K-5):
        cases = list(combinations(others, len(others)))
    else:
        cases = list(combinations(others, K - 5))
    for case in cases:
        al = deepcopy(alphabet)
        word_num = N
        for c in case:
            al[ord(c) - 97] = True
        for word in words:
            for w in word:
                if not al[ord(w) - 97]:
                    word_num -= 1
                    break
        result = max(result, word_num)
    print(result)