room_list = input().split("|")
health = 100
bitcoins = 0
room_count = 0
complete = True
for room in room_list:
    Current_room = room.split()
    command = Current_room[0]
    number = int(Current_room[1])
    room_count += 1
    if command == "potion":
        current_health = health
        health_gained = number
        health += number
        if health > 100:
            health_gained = 100 - current_health
            health = 100

        print(f"You healed for {health_gained} hp.")
        print(f"Current health: {health} hp.")
    elif command == "chest":
        bitcoins += number
        print(f"You found {number} bitcoins.")
    else:
        health -= number
        if health > 0:
            print(f"You slayed {command}.")
        else:
            complete = False
            print(f"You died! Killed by {command}.")
            print(f"Best room: {room_count}")
            break

if complete:
    print(f"You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")
