import sys
input = sys.stdin.readline

# N개의 정의역 b개의 공역을 가지는 일대일 함수를 생각

N, b = map(int, input().split())

id = 0

for i in range(b+1):
    id += 2**i

if N <= id:
    print("yes")
else:
    print("no")