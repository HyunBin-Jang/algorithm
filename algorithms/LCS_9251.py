str1 = input()
str2 = input()

d = [[0 for _ in range(len(str1) + 1)] for _ in range(len(str2)+ 1)]
result = 0

for i in range(1, len(str1) + 1):
    for j in range(1, len(str2) + 1):
        if str1[i - 1] == str2[j - 1]:
            d[j][i] = d[j-1][i-1] + 1
        else:
            d[j][i] = max(d[j][i-1], d[j-1][i])

print(d[len(str2)][len(str1)])


# 다른 풀이
# from sys import stdin
# 
# 
# def main():
#     str_1 = stdin.readline().strip()
#     str_2 = stdin.readline().strip()
# 
#     dp = [0] * 1000
#     for char_1 in str_1:
#         max_count = 0
#         for j, char_2 in enumerate(str_2):
#             if max_count < dp[j]:
#                 max_count = dp[j]
#                 continue
#             if char_1 == char_2:
#                 dp[j] = max_count + 1
#     print(max(dp))
# 
# 
# if __name__ == "__main__":
#     main()
