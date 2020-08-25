budget = float(input())
flour_price = float(input())

eggs_price = 0.75 * flour_price
milk_price = 1.25 * flour_price / 4

cozonac_price = eggs_price + flour_price + milk_price
cozonac_count = 0
eggs_count = 0
while budget >= cozonac_price:

    cozonac_price = eggs_price + flour_price + milk_price
    cozonac_count += 1
    eggs_count += 3
    budget -= cozonac_price
    if cozonac_count % 3 == 0:
        eggs_count -= cozonac_count - 2

print(f"You made {cozonac_count} cozonacs! Now you have {eggs_count} eggs and {budget:.2f}BGN left.")
