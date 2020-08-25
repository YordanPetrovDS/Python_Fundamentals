cards_list = input().split(":")
command = input()
cards = []
while command != "Ready":
    arg = command.split()

    if arg[0] == "Add":
        if arg[1] in cards_list:
            cards.append(arg[1])
        else:
            print(f"Card not found.")
    elif arg[0] == "Insert":
        index = int(arg[2])
        if (0 <= index < len(cards)) and arg[1] in cards_list:
            cards.insert(index, arg[1])
        else:
            print(f"Error!")
    elif arg[0] == "Remove":
        if arg[1] in cards_list and arg[1] in cards:
            cards.remove(arg[1])
        else:
            print(f"Card not found.")
    elif arg[0] == "Swap":
        index1 = cards.index(arg[1])
        index2 = cards.index(arg[2])

        cards[index1], cards[index2] = cards[index2], cards[index1]
    elif (arg[0] + " " + arg[1]) == "Shuffle deck":
        cards.reverse()
    command = input()

print(f"{' '.join(cards)}")
