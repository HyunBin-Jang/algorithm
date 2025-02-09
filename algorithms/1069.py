import math
X, Y, D, T = map(int, input().split())

distance = math.sqrt(X**2 + Y**2)

def min_time(dist):
    case1 = 0             # D칸만큼 가다가 초당 1칸씩 이동
    case2 = 0            # 뒤로 좀 이동하다가 D칸의 배수만큼 바로 0으로 이동
    case3 = dist            # 초당 1칸씩만 이동

    if D/T <= 1:           # 점프보다 걷는게 빠른경우
        return dist


    if dist < D:
        case1 += min(dist % D, 2 * T)
    else:
        c1 = (dist // D - 1) * T + min(dist % D + D, 2 * T)
        c2 = (dist // D) * T + min(dist % D, 2 * T)
        case1 = min(c1, c2)

    case2 = (dist // D + 1) * T + min(((dist // D + 1) * D - dist), 2*T)

    return min(case1, case2, case3)

print(min_time(distance))