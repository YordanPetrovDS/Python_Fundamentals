items = input().split("|")
budget = float(input())
new_budget = budget
item_list = []
profit = 0

for item in items:
    current_item = item.split("->")
    obj = current_item[0]
    price = float(current_item[1])
    if (obj == "Clothes" and price <= 50) or (obj == "Shoes" and price <= 35) or (obj == "Accessories" and price <= 20.5):
        if budget >= price:
            budget -= price
            new_price = price * 1.4
            profit += new_price - price
            item_list.append(f'{new_price:.2f}')

new_budget += profit

print(*item_list)
print(f"Profit: {profit:.2f}")

if new_budget >= 150:
    print(f"Hello, France!")
else:
    print(f"Time to go.")
