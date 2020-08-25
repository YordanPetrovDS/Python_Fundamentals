destinations = input()

while True:

    input_command = input()

    if input_command == "Travel":
        break

    arg = input_command.split(":")
    command = arg[0]

    if command == "Add Stop":
        index = int(arg[1])
        string = arg[2]
        if 0 <= index < len(destinations):
            destinations = destinations[:index] + string + destinations[index:]
        print(destinations)
    elif command == "Remove Stop":
        start_index = int(arg[1])
        end_index = int(arg[2])
        if 0 <= start_index < len(destinations) and 0 < end_index < len(destinations):
            destinations = destinations[:start_index] + destinations[end_index + 1:]
        print(destinations)
    elif command == "Switch":
        old_string = arg[1]
        new_string = arg[2]
        destinations = destinations.replace(old_string, new_string)
        print(destinations)

print(f"Ready for world tour! Planned stops: {destinations}")
