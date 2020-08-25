email = input()
input_command = input()

while input_command != "Complete":
    tokens = input_command.split()
    command = tokens[0]

    if command == "Make":
        action = tokens[1]
        if action == "Upper":
            email = email.upper()
        elif action == "Lower":
            email = email.lower()
        print(email)
    elif command == "GetDomain":
        count = int(tokens[1])
        if count < len(email):
            print(f"{email[-count:]}")
        else:
            print(email)
    elif command == "GetUsername":
        if "@" in email:
            arg = email.split("@")
            print(arg[0])
        else:
            print(f"The email {email} doesn't contain the @ symbol.")
    elif command == "Replace":
        char = tokens[1]
        email = email.replace(char, "-")
        print(email)
    elif command == "Encrypt":
        for char in email:
            print(ord(char), end=" ")

    input_command = input()
