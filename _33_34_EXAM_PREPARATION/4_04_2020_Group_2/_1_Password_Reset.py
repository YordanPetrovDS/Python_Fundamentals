password = input()

while True:

    input_command = input()

    if input_command == "Done":
        break

    arg = input_command.split()
    command = arg[0]

    if command == "TakeOdd":
        password_new = ""
        for index in range(len(password)):
            if index % 2 != 0:
                password_new += password[index]
        password = password_new
        print(password)
    elif command == "Cut":
        index = int(arg[1])
        length = int(arg[2])
        substring = password[index:index + length]
        password = password.replace(substring, "", 1)
        print(password)
    elif command == "Substitute":
        substring = arg[1]
        substitute = arg[2]

        if substring not in password:
            print("Nothing to replace!")
            continue

        password = password.replace(substring, substitute)
        print(password)

print(f"Your password is: {password}")
