import collections

dwarfs = {}
dwarf_name_hat_color_count = collections.defaultdict(int)

while True:
    data = input()
    if data == 'Once upon a time':
        break

    dwarf_name, dwarf_hat_color, dwarf_physics = data.split(' <:> ')
    dwarf_physics = int(dwarf_physics)

    key = (dwarf_name, dwarf_hat_color)
    dwarf_name_hat_color_count[key] += 1
    if key in dwarfs:
        if dwarfs[key] < dwarf_physics:
            dwarfs[key] = dwarf_physics
    else:
        dwarfs[key] = dwarf_physics


for key, value in sorted(dwarfs.items(), key=lambda item: (-item[1], -dwarf_name_hat_color_count[item[0]])):
    name, hat_color = key
    physics = value
    print(f'({hat_color}) {name} <-> {physics}')