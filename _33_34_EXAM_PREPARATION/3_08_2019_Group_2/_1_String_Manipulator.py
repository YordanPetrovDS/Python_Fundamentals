string = input()

while True:

    input_command = input()

    if input_command == "Done":
        break

    arg = input_command.split()
    command = arg[0]

    if command == "Change":
        char = arg[1]
        replacement = arg[2]
        string = string.replace(char, replacement)
        print(string)
    elif command == "Includes":
        check = arg[1]
        print(f"{check in string}")
    elif command == "End":
        check = arg[1]
        print(f"{check == string[len(string) - len(check):]}")
    elif command == "Uppercase":
        string = string.upper()
        print(string)
    elif command == "FindIndex":
        char = arg[1]
        print(f"{string.index(char)}")
    elif command == "Cut":
        index = int(arg[1])
        length = int(arg[2])
        string = string[index: index + length]
        print(string)
