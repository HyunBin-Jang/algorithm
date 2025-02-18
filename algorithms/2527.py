for _ in range(4):
    squares = list(map(int, input().split()))
    square1 = [(squares[0], squares[1]), (squares[2], squares[1]), (squares[0], squares[3]), (squares[2], squares[3])]
    square2 = [(squares[6],squares[7]), (squares[4],squares[7]), (squares[6], squares[5]), (squares[4], squares[5])]

    result = 'a'        # default
    if squares[0] == squares[6] or squares[2] == squares[4]:    # 'b'
        if squares[1] <= squares[7] <= squares[3] or squares[1] <= squares[5] <= squares[3]\
                or squares[5] <= squares[1] <=squares[7] or squares[5] <= squares[3] <= squares[7]:
            result = 'b'
    elif squares[3] == squares[5] or squares[1] == squares[7]:
        if squares[0] <= squares[4] <= squares[2] or squares[0] <= squares[6] <= squares[2]\
                or squares[4] <= squares[0] <=squares[6] or squares[4] <= squares[2] <=squares[6]:
            result = 'b'

    same = 0
    for i in range(4):        # 'c'
        if square1[i][0] == square2[i][0] and square1[i][1] == square2[i][1]:
            same += 1
    if same == 1:
        result = 'c'

                        # 'd'
    if squares[1] > squares[7] or squares[3] < squares[5] or squares[0] > squares[6] or squares[2] < squares[4]:
        result = 'd'

    print(result)