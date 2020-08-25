guests = {}
unlike_sum = 0
while True:
    input_command = input()

    if input_command == "Stop":
        break

    arg = input_command.split("-")
    guest = arg[1]
    meal = arg[2]
    command = arg[0]

    if command == "Like":
        if guest not in guests:
            guests[guest] = {}
            guests[guest][command] = []
            guests[guest][command].append(meal)
        else:
            if command not in guests[guest]:
                guests[guest][command] = []
                guests[guest][command].append(meal)
            else:
                if meal not in guests[guest][command]:
                    guests[guest][command].append(meal)
    elif command == "Unlike":
        if guest not in guests:
            print(f"{guest} is not at the party.")
        else:
            if "Like" not in guests[guest]:
                guests[guest]["Like"] = []

            if meal not in guests[guest]["Like"]:
                print(f"{guest} doesn't have the {meal} in his/her collection.")
            else:
                if command not in guests[guest]:
                    guests[guest][command] = []
                print(f"{guest} doesn't like the {meal}.")
                guests[guest][command].append(meal)
                guests[guest]["Like"].remove(meal)
                unlike_sum += 1

guests = dict(sorted(guests.items(), key=lambda x: (-len(x[1]["Like"]), x[0])))

[print(f"{guest}: " + ', '.join(guests[guest]["Like"])) for guest in guests]

print(f"Unliked meals: {unlike_sum}")
