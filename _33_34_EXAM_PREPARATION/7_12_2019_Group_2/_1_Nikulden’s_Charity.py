string = input()

input_command = input()

while input_command != "Finish":
    arg = input_command.split()
    command = arg[0]

    if command == "Replace":
        current_char = arg[1]
        new_char = arg[2]
        string = string.replace(current_char, new_char)
        print(string)
    elif command == "Cut":
        start_index = int(arg[1])
        end_index = int(arg[2])
        if 0 < start_index < len(string) and 0 < end_index < len(string):
            string = string[:start_index] + string[end_index + 1:]
            print(string)
        else:
            print("Invalid indexes!")
    elif command == "Make":
        action = arg[1]
        if action == "Upper":
            string = string.upper()
        elif action == "Lower":
            string = string.lower()
        print(string)
    elif command == "Check":
        string_check = arg[1]
        if string_check in string:
            print(f"Message contains {string_check}")
        else:
            print(f"Message doesn't contain {string_check}")
    elif command == "Sum":
        start_index = int(arg[1])
        end_index = int(arg[2])
        if 0 <= start_index < len(string) and 0 < end_index < len(string):
            substring = string[start_index:end_index+1]
            ascii_sum = 0
            for char in substring:
                ascii_sum += ord(char)
            print(ascii_sum)
        else:
            print("Invalid indexes!")
    input_command = input()
