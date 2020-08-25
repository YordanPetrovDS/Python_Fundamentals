skill = input()

input_command = input()

while input_command != "For Azeroth":
    arg = input_command.split()
    command = arg[0]

    if command == "GladiatorStance":
        skill = skill.upper()
        print(skill)
    elif command == "DefensiveStance":
        skill = skill.lower()
        print(skill)
    elif command == "Dispel":
        index = int(arg[1])
        letter = arg[2]
        if arg[1].isdigit() and letter.isalpha() and len(letter) == 1:
            if 0 <= index < len(skill):
                skill = skill.replace(skill[index], letter, 1)
                print("Success!")
            else:
                print("Dispel too weak.")
        else:
            print("Command doesn't exist!")
    elif command == "Target":
        action = arg[1]
        substring = arg[2]
        if action == "Change":
            second_substring = arg[3]
            skill = skill.replace(substring, second_substring)
            print(skill)
        elif action == "Remove":
            skill = skill.replace(substring, "")
            print(skill)
        else:
            print("Command doesn't exist!")
    else:
        print("Command doesn't exist!")

    input_command = input()
