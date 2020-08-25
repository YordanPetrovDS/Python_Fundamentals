targets = list(map(int, input().split("|")))
command = input()
points = 0
while command != "Game over":
    current_command = command.split()
    if current_command[0] == "Shoot":
        current_split = current_command[1].split("@")
        direction = current_split[0]
        start_index = int(current_split[1])
        length = int(current_split[2])

        if direction == "Left":
            if 0 <= start_index < len(targets):
                if (start_index - length) < 0:
                    current_index = (start_index - length) % len(targets)
                else:
                    current_index = start_index - length

                if targets[current_index] < 5:
                    points += targets[current_index]
                    targets[current_index] = 0
                else:
                    points += 5
                    targets[current_index] -= 5

        elif direction == "Right":
            if 0 <= start_index < len(targets):
                if (start_index + length) > len(targets):
                    current_index = (start_index + length) % len(targets)
                else:
                    current_index = start_index + length

                if targets[current_index] < 5:
                    points += targets[current_index]
                    targets[current_index] = 0
                else:
                    points += 5
                    targets[current_index] -= 5

    elif current_command[0] == "Reverse":
        targets.reverse()
    command = input()

print(f"{' - '.join(map(str, targets))}")
print(f"Iskren finished the archery tournament with {points} points!")
