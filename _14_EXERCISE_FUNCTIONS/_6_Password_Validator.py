def password_validator(password_input):
    check_1 = True
    check_2 = True
    check_3 = True
    digits_count = 0
    if len(password_input) < 6 or len(password_input) > 10:
        check_1 = False
        print("Password must be between 6 and 10 characters")

    for i in password_input:
        if 97 <= ord(i.lower()) <= 122 or 48 <= ord(i) <= 57:
            pass
        else:
            check_2 = False

        if 48 <= ord(i) <= 57:
            digits_count += 1
    if digits_count < 2:
        check_3 = False

    if not check_2:
        print("Password must consist only of letters and digits")

    if not check_3:
        print("Password must have at least 2 digits")

    if check_1 and check_2 and check_3:
        print("Password is valid")


password = input()
password_validator(password)
