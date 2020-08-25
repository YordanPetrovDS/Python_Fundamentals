friend_list = input().split(", ")


def blacklist(friend_name):
    if friend_name in friend_list:
        for x in range(len(friend_list)):
            to_black_list = friend_list[x]
            if to_black_list == friend_name:
                friend_list[x] = "Blacklisted"
                print(f"{friend_name} was blacklisted.")

    elif friend_name not in friend_list:
        print(f"{friend_name} was not found.")


def error(name_index):
    if 0 <= name_index <= (len(friend_list) - 1):
        for x in range(len(friend_list)):
            lost_name = friend_list[x]
            if x == name_index and lost_name != "Lost" and lost_name != "Blacklisted":
                print(f"{lost_name} was lost due to an error.")
                friend_list[name_index] = "Lost"
                break


def change(name_index, new_name):
    if 0 <= name_index <= (len(friend_list) - 1):
        for x in range(len(friend_list)):
            current_name = friend_list[x]
            if x == name_index:
                print(f"{current_name} changed his username to {new_name}.")
                friend_list[x] = new_name


while True:
    line = input()
    if line == "Report":
        blacklisted_users = [blacklist for blacklist in friend_list if blacklist == "Blacklisted"]
        lost_users = [lost for lost in friend_list if lost == "Lost"]
        print(f"Blacklisted names: {len(blacklisted_users)}")
        print(f"Lost names: {len(lost_users)}")
        print(f"{' '.join(friend_list)}")
        break

    else:
        tokens = line.split()
        command = tokens[0]

        if command == "Blacklist":
            name = tokens[1]
            blacklist(name)

        elif command == "Error":
            index = int(tokens[1])
            error(index)

        elif command == "Change":
            index = int(tokens[1])
            name = tokens[2]
            change(index, name)