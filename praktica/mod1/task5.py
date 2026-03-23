prices = list(map(int, input().split()))
K = int(input())
M = int(input())
discount = []
for price in prices:
    discount_price = price - (price // K) * M
    discount.append(discount_price)
print(prices)
print(discount)