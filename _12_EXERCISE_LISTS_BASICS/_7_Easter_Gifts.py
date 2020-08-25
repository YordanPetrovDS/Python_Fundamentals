gifts_list = input().split()
command = input()

while command != "No Money":

    command_split = command.split()

    if command_split[0] == "OutOfStock":
        gifts_list = ["None" if item == command_split[1] else item for item in gifts_list]
    elif command_split[0] == "Required":
        if int(command_split[2]) >= 0 and (int(command_split[2]) <= len(gifts_list) - 1):
            gifts_list[int(command_split[2])] = command_split[1]
    elif command_split[0] == "JustInCase":
        gifts_list[len(gifts_list) - 1] = command_split[1]
    command = input()

gifts_list = [item for item in gifts_list if item != "None"]

print(' '.join(gifts_list))
