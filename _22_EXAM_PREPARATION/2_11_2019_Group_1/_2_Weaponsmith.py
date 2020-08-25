parts_list = input().split("|")
command = input()

while command != "Done":
    action = command.split()

    if action[0] == "Move":
        index = int(action[2])
        if 0 <= index < len(parts_list):
            if action[1] == "Left":
                if index > 0:
                    parts_list[index], parts_list[index - 1] = parts_list[index - 1], parts_list[index]
            elif action[1] == "Right":
                if index < len(parts_list) - 1:
                    parts_list[index], parts_list[index + 1] = parts_list[index + 1], parts_list[index]
    elif action[0] == "Check":
        if action[1] == "Even":
            print(f"{' '.join([el for index, el in enumerate(parts_list) if index % 2 == 0])}")
        elif action[1] == "Odd":
            print(f"{' '.join([el for index, el in enumerate(parts_list) if index % 2 != 0])}")
    command = input()

print(f"You crafted {''.join(parts_list)}!")
