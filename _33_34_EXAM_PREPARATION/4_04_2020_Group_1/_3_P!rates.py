cities = {}

while True:
    input_city = input()

    if input_city == "Sail":
        break

    arg = input_city.split("||")
    city = arg[0]
    population = int(arg[1])
    gold = int(arg[2])

    if city not in cities:
        cities[city] = {}
        cities[city]["population"] = population
        cities[city]["gold"] = gold
    else:
        cities[city]["population"] += population
        cities[city]["gold"] += gold

while True:
    input_command = input()

    if input_command == "End":
        break

    arg = input_command.split("=>")
    command = arg[0]
    town = arg[1]

    if command == "Plunder":
        people = int(arg[2])
        gold = int(arg[3])
        cities[town]["population"] -= people
        cities[town]["gold"] -= gold

        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
        if cities[town]["population"] == 0 or cities[town]["gold"] == 0:
            cities.pop(town)
            print(f"{town} has been wiped off the map!")

    elif command == "Prosper":
        gold = int(arg[2])
        if gold < 0:
            print("Gold added cannot be a negative number!")
            continue
        cities[town]["gold"] += gold
        print(f"{gold} gold added to the city treasury. {town} now has {cities[town]['gold']} gold.")

if len(cities) == 0:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
else:
    cities = dict(sorted(cities.items(), key=lambda x: (-x[1]['gold'], x[0])))
    print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")
    [print(f"{town} -> Population: {str(cities[town]['population'])} citizens, Gold: {str(cities[town]['gold'])} kg")
     for town in cities]
