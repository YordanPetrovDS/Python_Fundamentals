users = {}
while True:

    input_command = input()

    if input_command == "Results":
        break

    arg = input_command.split(":")
    command = arg[0]
    username = arg[1]

    if command == "Add":
        health = int(arg[2])
        energy = int(arg[3])
        if username not in users:
            users[username] = {}
            users[username]["health"] = health
            users[username]["energy"] = energy
        else:
            users[username]["health"] += health
    elif command == "Attack":
        defender_name = arg[2]
        damage = int(arg[3])
        if username in users and defender_name in users:
            users[defender_name]["health"] -= damage
            users[username]["energy"] -= 1

            if users[defender_name]["health"] <= 0:
                users.pop(defender_name)
                print(f"{defender_name} was disqualified!")

            if users[username]["energy"] == 0:
                users.pop(username)
                print(f"{username} was disqualified!")

    elif command == "Delete":
        if username == "All":
            users.clear()
        elif username in users:
            users.pop(username)

users = dict(sorted(users.items(), key=lambda x: (-x[1]["health"], x[0])))

print(f"People count: {len(users)}")
[print(f"{user} - {str(users[user]['health'])} - {str(users[user]['energy'])}") for user in users]
