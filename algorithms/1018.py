N, M = map(int, input().split())
board = []
chess_1 = ["WBWBWBWB","BWBWBWBW","WBWBWBWB","BWBWBWBW","WBWBWBWB","BWBWBWBW","WBWBWBWB","BWBWBWBW"]
chess_2 = ["BWBWBWBW","WBWBWBWB","BWBWBWBW","WBWBWBWB","BWBWBWBW","WBWBWBWB","BWBWBWBW","WBWBWBWB"]

for _ in range(N):
    board.append(input())

def paint(start_i, start_j):
    result_1 = 0
    result_2 = 0
    for i in range(8):
        for j in range(8):
            if board[i + start_i][j + start_j] != chess_1[i][j]:
                result_1 += 1
            if board[i + start_i][j + start_j] != chess_2[i][j]:
                result_2 += 1

    return min(result_1, result_2)

result = 2501
for i in range(N - 7):
    for j in range(M - 7):
        result = min(result, paint(i, j))

print(result)