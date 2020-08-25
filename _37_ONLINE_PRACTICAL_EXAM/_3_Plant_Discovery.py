n = int(input())
plants = {}
for i in range(n):
    plant, rarity = input().split("<->")
    plants[plant] = {}
    plants[plant]['rarity'] = int(rarity)
    plants[plant]['rating'] = []

while True:
    input_command = input()

    if input_command == "Exhibition":
        break

    tokens = input_command.split(": ")
    command = tokens[0]
    if command == "Rate":
        arg = tokens[1].split(" - ")
        plant = arg[0]
        rating = int(arg[1])
        if plant not in plants:
            print("error")
            continue
        plants[plant]['rating'].append(rating)

    elif command == "Update":
        arg = tokens[1].split(" - ")
        plant = arg[0]
        new_rarity = int(arg[1])
        if plant not in plants:
            print("error")
            continue
        plants[plant]['rarity'] = new_rarity
    elif command == "Reset":
        plant = tokens[1]
        if plant not in plants:
            print("error")
            continue
        plants[plant]['rating'].clear()
    else:
        print("error")

for key in plants:
    if not plants[key]['rating']:
        plants[key]['rating'] = 0
    else:
        plants[key]['rating'] = sum(plants[key]['rating']) / len(plants[key]['rating'])

plants = dict(sorted(plants.items(), key=lambda x: (-x[1]['rarity'], -x[1]['rating'])))

print(f"Plants for the exhibition:")
[print(f"- {plant}; Rarity: {str(plants[plant]['rarity'])}; Rating: {plants[plant]['rating']:.2f}") for plant in plants]
