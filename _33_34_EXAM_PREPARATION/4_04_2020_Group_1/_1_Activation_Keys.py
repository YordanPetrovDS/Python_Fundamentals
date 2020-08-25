string = input()

while True:
    input_command = input()

    if input_command == "Generate":
        break

    arg = input_command.split(">>>")

    command = arg[0]

    if command == "Contains":
        substring = arg[1]
        if substring not in string:
            print("Substring not found!")
            continue
        print(f"{string} contains {substring}")
    elif command == "Flip":
        case = arg[1]
        start_index = int(arg[2])
        end_index = int(arg[3])
        if case == "Upper":
            string = string[:start_index] + string[start_index:end_index].upper() + string[end_index:]
        elif case == "Lower":
            string = string[:start_index] + string[start_index:end_index].lower() + string[end_index:]
        print(string)
    elif command == "Slice":
        start_index = int(arg[1])
        end_index = int(arg[2])
        string = string[:start_index] + string[end_index:]
        print(string)

print(f"Your activation key is: {string}")
