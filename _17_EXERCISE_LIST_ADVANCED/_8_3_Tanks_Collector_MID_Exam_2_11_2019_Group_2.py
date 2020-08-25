def index_is_in_range(index, lenght):
    return 0 <= index < lenght


tanks = input().split(", ")
commands_count = int(input())

for _ in range(commands_count):
    args = input().split(", ")
    command = args[0]

    if command == "Add":
        tank_name = args[1]
        if tank_name in tanks:
            print('Tank is already bought')
            continue

        tanks.append(tank_name)
        print("Tank successfully bought")
    elif command == "Remove":
        tank_name = args[1]
        if tank_name not in tanks:
            print("Tank not found")
            continue

        tanks.remove(tank_name)
        print("Tank successfully sold")

    elif command == "Remove At":
        index = int(args[1])
        if not index_is_in_range(index, len(tanks)):
            print("Index out of range")
            continue

        tanks.pop(index)
        print("Tank successfully sold")

    elif command == "Insert":
        index = int(args[1])
        tank_name = args[2]

        if not index_is_in_range(index, len(tanks)):
            print("Index out of range")
            continue

        if tank_name in tanks:
            print("Tank is already bought")
            continue

        tanks.insert(index, tank_name)
        print("Tank successfully bought")

print(", ".join(tanks))
