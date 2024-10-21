X = int(input())

stick = [64]

while sum(stick) > X:
    i = stick.pop()
    stick.append(i / 2)
    if sum(stick) < X:
        stick.append(i / 2)

print(len(stick))