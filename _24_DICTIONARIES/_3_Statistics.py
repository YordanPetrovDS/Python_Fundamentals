from _collections import defaultdict

stocks = defaultdict(int)  # if there is no such key, then key = 0

while True:
    command = input()
    if command == "statistics":
        break
    product, quantity = command.split(": ")
    stocks[product] += int(quantity)

# stocks = {}

# while True:
#     command = input()
#     if command == "statistics":
#         break
#
#     product, quantity = command.split(": ")
#
#     if product in stocks:
#         stocks[product] += int(quantity)
#     else:
#         stocks[product] = int(quantity)

print(f"Products in stock:")
[print(f"- {product}: {quantity}") for product, quantity in stocks.items()]
print(f"Total Products: {len(stocks.keys())}")
print(f"Total Quantity: {sum(stocks.values())}")
