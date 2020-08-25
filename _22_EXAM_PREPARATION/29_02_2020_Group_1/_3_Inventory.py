items = input().split(", ")

input_command = input()

while input_command != "Craft!":
    args = input_command.split(" - ")

    if args[0] == "Collect":
        if args[1] not in items:
            items.append(args[1])
    elif args[0] == "Drop":
        if args[1] in items:
            items.remove(args[1])
    elif args[0] == "Combine Items":
        item_split = args[1].split(":")
        old_item = item_split[0]
        new_item = item_split[1]
        if old_item in items:
            if items.index(old_item) == (len(items) - 1):
                items.append(new_item)
            else:
                items.insert((items.index(old_item)) + 1, new_item)
    elif args[0] == "Renew":
        if args[1] in items:
            items.remove(args[1])
            items.append(args[1])

    input_command = input()

print(f" {', '.join(items)}")
