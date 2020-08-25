string = input()
command = input()

while command != "Reveal":
    tokens = command.split(":|:")
    command_ = tokens[0]

    if command_ == "InsertSpace":
        index = int(tokens[1])
        string = string[:index] + " " + string[index:]
        print(string)
    elif command_ == "Reverse":
        substring = tokens[1]
        if substring in string:
            string = string.replace(substring, "", 1) + substring[::-1]
            print(string)
        else:
            print("error")
    elif command_ == "ChangeAll":
        substring = tokens[1]
        replacement = tokens[2]
        string = string.replace(substring, replacement)
        print(string)
    command = input()
print(f"You have a new text message: {string}")
