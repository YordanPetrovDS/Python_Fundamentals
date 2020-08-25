def get_stock(raw_data):
    data = raw_data.split(' ')
    return {data[i]: data[i + 1] for i in range(0, len(data), 2)}


def check_availability(stock: dict, searched_products: list):
    return '\n'.join([
        f"Sorry, we don't have {product}"
        if not stock.get(product)
        else f"We have {stock[product]} of {product} left"
        for product in searched_products])
    # for product in searched_products:
    #     if not stock.get(product):
    #         print(f"Sorry, we don't have {product}")
    #     else:
    #         print(f"We have {stock[product]} of {product} left")


stock = get_stock(input())

print(check_availability(stock, input().split(' ')))

# elements = input().split()
#
# bakery = {}
#
# for i in range(0, len(elements), 2):
#     key = elements[i]
#     value = elements[i + 1]
#     bakery[key] = int(value)
#
# searched_products = input().split()
#
# for product in searched_products:
#     if product in bakery:
#         print(f"We have {bakery[product]} of {product} left")
#     else:
#         print(f"Sorry, we don't have {product}")
