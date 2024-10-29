B, C, D = map(int, input().split())
min_num = min(B, C, D)
Burger = list(map(int, input().split()))
Side = list(map(int, input().split()))
Beverage = list(map(int, input().split()))

normal_price = 0
normal_price += sum(Burger)
normal_price += sum(Side)
normal_price += sum(Beverage)
Burger.sort(reverse=True)
Side.sort(reverse=True)
Beverage.sort(reverse=True)

discount_price = normal_price
for i in range(min_num):
    discount_price -= Burger[i] * 0.1
    discount_price -= Side[i] * 0.1
    discount_price -= Beverage[i] * 0.1

print(normal_price)
print(int(discount_price))