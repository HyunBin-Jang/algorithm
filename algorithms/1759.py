from itertools import combinations
L, C = map(int, input().split())
alphabet = set(input().split())
result = set()
vowels = ['a', 'e', 'i', 'o', 'u']
vowel = []
consonant = []
for a in alphabet:
    if a in vowels:
        vowel.append(a)
    else:
        consonant.append(a)

for v in vowel:
    for i in range(len(consonant)-1):
        for j in range(i+1, len(consonant)):
            tmp = ""
            s = alphabet.copy()
            tmp += v
            s -= set(v)
            tmp += consonant[i]
            tmp += consonant[j]
            s -= set(consonant[i])
            s -= set(consonant[j])
            c = list(combinations(s, L-3))

            for a in c:
                k = ""
                for d in a:
                    k += d
                result.add(''.join(sorted(tmp + k)))

result = list(result)
result.sort()
for r in result:
    print(r)