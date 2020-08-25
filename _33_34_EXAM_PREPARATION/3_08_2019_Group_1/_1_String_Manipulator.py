string = input()

while True:

    input_command = input()

    if input_command == "End":
        break
    arg = input_command.split()

    command = arg[0]

    if command == "Translate":
        char = arg[1]
        replacement = arg[2]
        string = string.replace(char, replacement)
        print(string)
    elif command == "Includes":
        string_new = arg[1]
        print(f"{string_new in string}")
    elif command == "Start":
        string_new = arg[1]
        print(f"{string_new == string[:len(string_new)]}")
    elif command == "Lowercase":
        string = string.lower()
        print(string)
    elif command == "FindIndex":
        char = arg[1]
        print(string.rindex(char))
    elif command == "Remove":
        start_index = int(arg[1])
        length = int(arg[2])
        string = string[:start_index] + string[start_index + length:]
        print(string)
