username = input()
input_command = input()
while input_command != "Sign up":
    tokens = input_command.split()
    command = tokens[0]

    if command == "Case":
        case = tokens[1]
        if case == "lower":
            username = username.lower()
        else:
            username = username.upper()
        print(username)
    elif command == "Reverse":
        start_index = int(tokens[1])
        end_index = int(tokens[2])
        if 0 < start_index < len(username) or 0 < end_index < len(username):
            reversed_username = username[start_index:end_index+1]
            reversed_username = reversed_username[::-1]
            print(reversed_username)
    elif command == "Cut":
        substring = tokens[1]
        if substring in username:
            username = username.replace(substring, "")
            print(username)
        else:
            print(f"The word {username} doesn't contain {substring}.")
    elif command == "Replace":
        char = tokens[1]
        username = username.replace(char, "*")
        print(username)
    elif command == "Check":
        char = tokens[1]
        if char in username:
            print("Valid")
        else:
            print(f"Your username must contain {char}.")

    input_command = input()
