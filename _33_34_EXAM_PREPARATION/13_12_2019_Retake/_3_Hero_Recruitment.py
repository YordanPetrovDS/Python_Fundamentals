heroes = {}
while True:
    input_command = input()

    if input_command == "End":
        break

    tokens = input_command.split()
    command = tokens[0]
    hero_name = tokens[1]

    if command == "Enroll":
        if hero_name not in heroes:
            heroes[hero_name] = []
        else:
            print(f"{hero_name} is already enrolled.")
    elif command == "Learn":
        spell_name = tokens[2]
        if hero_name not in heroes:
            print(f"{hero_name} doesn't exist.")
        else:
            if spell_name in heroes[hero_name]:
                print(f"{hero_name} has already learnt {spell_name}.")
            else:
                heroes[hero_name].append(spell_name)
    elif command == "Unlearn":
        spell_name = tokens[2]
        if hero_name not in heroes:
            print(f"{hero_name} doesn't exist.")
        else:
            if spell_name not in heroes[hero_name]:
                print(f"{hero_name} doesn't know {spell_name}.")
            else:
                heroes[hero_name].remove(spell_name)

heroes = dict(sorted(heroes.items(), key=lambda x: (-len(x[1]), x[0])))

print("Heroes:")
[(print(f"== {hero}: ", end=""), print(', '.join(heroes[hero]))) for hero in heroes]
