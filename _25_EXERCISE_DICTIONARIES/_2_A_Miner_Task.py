from _collections import defaultdict

my_dict = defaultdict(int)

while True:
    resource = input()

    if resource == "stop":
        break

    quantity = int(input())

    my_dict[resource] += quantity

[print(f"{resource} -> {quantity}") for resource, quantity in my_dict.items()]