n = int(input())
parking_dict = {}

for _ in range(n):
    command = input().split()
    if command[0] == "register":
        if command[1] in parking_dict:
            print(f"ERROR: already registered with plate number {command[2]}")
        else:
            parking_dict[command[1]] = command[2]
            print(f"{command[1]} registered {command[2]} successfully")
    elif command[0] == "unregister":
        if command[1] in parking_dict:
            print(f"{command[1]} unregistered successfully")
            parking_dict.pop(command[1])
        else:
            print(f"ERROR: user {command[1]} not found")

[print(f"{name} => {car}") for name, car in parking_dict.items()]
