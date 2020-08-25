capacity = int(input())
users = {}
while True:
    input_command = input()

    if input_command == "Statistics":
        break

    arg = input_command.split("=")
    command = arg[0]

    if command == "Add":
        username = arg[1]
        sent = int(arg[2])
        received = int(arg[3])
        if username in users:
            continue

        users[username] = {}
        users[username]["sent"] = sent
        users[username]["received"] = received
    elif command == "Message":
        sender = arg[1]
        receiver = arg[2]
        if sender not in users or receiver not in users:
            continue
        users[sender]["sent"] += 1
        users[receiver]["received"] += 1

        if (users[sender]["sent"] + users[sender]["received"]) >= capacity:
            print(f"{sender} reached the capacity!")
            users.pop(sender)

        if (users[receiver]["sent"] + users[receiver]["received"]) >= capacity:
            print(f"{receiver} reached the capacity!")
            users.pop(receiver)

    elif command == "Empty":
        username = arg[1]
        if username != "All":
            users.pop(username)
        else:
            users.clear()

users = dict(sorted(users.items(), key=lambda x: (-x[1]["received"], x[0])))

print(f"Users count: {len(users)}")
[print(f"{user} - {users[user]['sent'] + users[user]['received']}") for user in users]
