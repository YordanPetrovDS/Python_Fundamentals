from _collections import defaultdict

name_quantity = defaultdict(float)
name_price = defaultdict(float)
orders = input()
my_dict = {}
while orders != "buy":
    args = orders.split()

    quantity = float(args[2])
    price = float(args[1])

    name_price[args[0]] = price
    name_quantity[args[0]] += quantity

    orders = input()

for i in name_price.keys():
    my_dict[i] = name_price[i] * name_quantity[i]

[print(f"{product} -> {quantity:.2f}") for product, quantity in my_dict.items()]
