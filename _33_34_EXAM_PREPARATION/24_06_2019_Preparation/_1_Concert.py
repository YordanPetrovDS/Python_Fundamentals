bands = {}
total_time = 0
while True:

    input_command = input()

    if input_command == "start of concert":
        break

    arg = input_command.split("; ")

    command = arg[0]
    band_name = arg[1]

    if command == "Add":
        band_members = arg[2].split(", ")
        if band_name not in bands:
            bands[band_name] = {}
            bands[band_name]['members'] = []
            for member in band_members:
                if member not in bands[band_name]['members']:
                    bands[band_name]['members'].append(member)
        else:
            if 'members' not in bands[band_name]:
                bands[band_name]['members'] = []
            for member in band_members:
                if member not in bands[band_name]['members']:
                    bands[band_name]['members'].append(member)
    elif command == "Play":
        time = int(arg[2])
        if band_name not in bands:
            bands[band_name] = {}
            bands[band_name]['time'] = time
            total_time += time
        else:
            if 'time' not in bands[band_name]:
                bands[band_name]['time'] = 0
            bands[band_name]['time'] += time
            total_time += time

bands = dict(sorted(bands.items(), key=lambda x: (-x[1]['time'], x[0])))
current_band = input()


print(f"Total time: {total_time}")
[print(f"{band} -> {str(bands[band]['time'])}") for band in bands]

print(f"{current_band}"),
[print(f"=> {member}") for member in bands[current_band]['members']]
