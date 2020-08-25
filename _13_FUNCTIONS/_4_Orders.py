product_input = input()
quantity_input = int(input())


def total_price(product, quantity):
    result = 0
    if product == "coffee":
        result = 1.5 * quantity
    elif product == "water":
        result = 1 * quantity
    elif product == "coke":
        result = 1.40 * quantity
    elif product == "snacks":
        result = 2 * quantity

    return result


print(f"{total_price(product_input, quantity_input):.2f}")
