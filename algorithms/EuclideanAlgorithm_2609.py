A, B = map(int, input().split())
a, b = 0, 0

if A >= b:
    a = A
    b = B
else:
    a = B
    b = A

#유클리드 호제법 : 2개의 자연수 a, b(a > b)에 대해서 a를 b로 나눈 나머지가 r일 때,
# a와 b의 최대공약수는 b와 r의 최대공약수와 같다.

r = a % b
while r != 0:
    tmp = r
    r = b % r
    b = tmp

GCD = b
print(GCD)

#  두 수 a와 b의 최소공배수는 a와 b의 곱을 a와 b의 최대공약수를 나눈 것과 같다.
LCM = (A * B) // GCD
print(LCM)