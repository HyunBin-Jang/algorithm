strs = input()
croatia_al = ['c=', 'c-', 'dz=','d-','lj','nj','s=','z=']
length = len(strs)
result = 0
for c in croatia_al:
    while c in strs:
        strs = strs.replace(c, '1', 1)
        result += 1
        length -= len(c)
result += length
print(result)