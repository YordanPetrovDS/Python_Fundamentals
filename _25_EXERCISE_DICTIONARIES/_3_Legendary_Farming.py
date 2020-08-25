def validate_key_existing(dictionary, key, def_value=0):
    if key not in dictionary:
        dictionary[key] = def_value


key_materials = {
    'fragments': 0,
    'shards': 0,
    'motes': 0
}

legendary_items = {
    'fragments': 'Valanyr',
    'shards': 'Shadowmourne',
    'motes': 'Dragonwrath'
}

junks = {}
winner = ""

while winner == "":
    args = input().lower().split()
    for i in range(0, len(args), 2):
        quantity = int(args[i])
        material = args[i + 1]

        if material in key_materials:
            key_materials[material] += quantity

            if key_materials[material] >= 250:
                winner = material
                break
        else:
            validate_key_existing(junks, material)
            junks[material] += quantity

key_materials[winner] -= 250

print(f"{legendary_items[winner]} obtained!")

# "-" сортиране в низходящ ред, по два критерия, само на числови стойности;

key_materials = dict(sorted(key_materials.items(), key=lambda el: (-el[1], el[0])))
junks = dict(sorted(junks.items()))

[print(f"{resource}: {quantity}") for resource, quantity in key_materials.items()]
[print(f"{resource}: {quantity}") for resource, quantity in junks.items()]
