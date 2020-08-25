events_list = input().split("|")

coins = 100
energy = 100
success = True
for event in events_list:
    current_event = event.split("-")
    event_type = current_event[0]
    event_value = int(current_event[1])

    if event_type == "rest":
        current_energy = energy
        energy += event_value
        if energy > 100:
            gained_energy = 100 - current_energy
            print(f"You gained {gained_energy} energy.")
            print(f"Current energy: 100.")
            energy = 100
        else:
            print(f"You gained {event_value} energy.")
            print(f"Current energy: {energy}.")
    elif event_type == "order":
        if energy >= 30:
            print(f"You earned {event_value} coins.")
            energy -= 30
            coins += event_value
        else:
            energy += 50
            print(f"You had to rest!")
    else:
        if coins > event_value:
            print(f"You bought {event_type}.")
            coins -= event_value
        else:
            print(f"Closed! Cannot afford {event_type}.")
            success = False
            break
if success:
    print(f"Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")
