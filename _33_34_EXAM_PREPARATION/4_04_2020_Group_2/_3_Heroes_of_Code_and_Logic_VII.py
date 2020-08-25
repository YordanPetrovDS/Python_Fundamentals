n = int(input())

heroes = {}

for i in range(n):
    hero_input = input()

    arg = hero_input.split()
    hero_name = arg[0]
    HP = int(arg[1])
    MP = int(arg[2])
    heroes[hero_name] = {}
    heroes[hero_name]['HP'] = HP
    heroes[hero_name]['MP'] = MP

while True:
    input_command = input()

    if input_command == "End":
        break

    arg = input_command.split(" - ")
    command = arg[0]
    hero_name = arg[1]

    if command == "CastSpell":
        MP_needed = int(arg[2])
        spell_name = arg[3]
        if heroes[hero_name]['MP'] < MP_needed:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")
            continue

        heroes[hero_name]['MP'] -= MP_needed
        print(f"{hero_name} has successfully cast {spell_name} and now has {str(heroes[hero_name]['MP'])} MP!")

    elif command == "TakeDamage":
        damage = int(arg[2])
        attacker = arg[3]
        heroes[hero_name]['HP'] -= damage

        if heroes[hero_name]['HP'] <= 0:
            heroes.pop(hero_name)
            print(f"{hero_name} has been killed by {attacker}!")
            continue

        print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {str(heroes[hero_name]['HP'])} HP left!")

    elif command == "Recharge":
        amount = int(arg[2])
        current_MP = heroes[hero_name]['MP']
        heroes[hero_name]['MP'] += amount

        if heroes[hero_name]['MP'] > 200:
            heroes[hero_name]['MP'] = 200
            amount = 200 - current_MP

        print(f"{hero_name} recharged for {amount} MP!")

    elif command == "Heal":
        amount = int(arg[2])
        current_HP = heroes[hero_name]['HP']
        heroes[hero_name]['HP'] += amount

        if heroes[hero_name]['HP'] > 100:
            heroes[hero_name]['HP'] = 100
            amount = 100 - current_HP

        print(f"{hero_name} healed for {amount} HP!")

heroes = dict(sorted(heroes.items(), key=lambda x: (-x[1]['HP'], x[0])))

[(print(f"{hero}"), [print(f"  {attribute}: {heroes[hero][attribute]}") for attribute in heroes[hero]]) for hero in heroes]
