x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

result = 0

if x2 - x1 > 0 :
    if (y2 - y1)/(x2 - x1) == (y3 - y2)/(x3 - x2):
        result = 0
    elif y3 > (y2-y1)/(x2 - x1)*(x3 - x1) + y1:
        result = 1
    elif y3 < (y2-y1)/(x2 - x1)*(x3 - x1) + y1:
        result = -1
elif x2 - x1 < 0 :
    if (y2 - y1)/(x2 - x1) == (y3 - y2)/(x3 - x2):
        result = 0
    elif y3 < (y2-y1)/(x2 - x1)*(x3 - x1) + y1:
        result = 1
    elif y3 > (y2-y1)/(x2 - x1)*(x3 - x1) + y1:
        result = -1
elif x2 - x1 == 0 and y2 - y1 >0:
    if x3 < x1:
        result = 1
    elif x3 > x1:
        result = -1
elif x2 - x1 == 0 and y2 - y1 <0:
    if x3 > x1:
        result = 1
    elif x3 < x1:
        result = -1

print(result)