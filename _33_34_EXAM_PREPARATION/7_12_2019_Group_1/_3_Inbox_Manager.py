line = input()
users_dict = {}
while line != "Statistics":
    args = line.split("->")
    command = args[0]
    username = args[1]

    if command == "Add":
        if username in users_dict:
            print(f"{username} is already registered")
        else:
            users_dict[username] = []
    elif command == "Send":
        email = args[2]
        if username not in users_dict:
            users_dict[username] = []
        users_dict[username].append(email)
    elif command == "Delete":
        if username in users_dict:
            users_dict.pop(username)
        else:
            print(f"{username} not found!")
    line = input()

users_dict = dict(sorted(users_dict.items(), key=lambda x: (-len(x[1]), x[0])))
print(f"Users count: {len(users_dict)}")

# for user in users_dict:
#     print(f"{user}")
#     for email in users_dict[user]:
#         print(f" - {email}")

[(print(f"{user}"), [print(f" - {email}") for email in users_dict[user]]) for user in users_dict]
