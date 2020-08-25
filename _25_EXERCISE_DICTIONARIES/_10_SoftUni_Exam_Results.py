command = input()

people_res = {}
language_sub = {}

while command != "exam finished":
    arg = command.split("-")

    if len(arg) == 3:
        username = arg[0]
        language = arg[1]
        points = int(arg[2])

        if username not in people_res:
            people_res[username] = points
        elif people_res[username] < points:
            people_res[username] = points

        if language not in language_sub:
            language_sub[language] = 1
        else:
            language_sub[language] += 1

    else:
        people_res.pop(arg[0])

    command = input()

people_res = dict(sorted(people_res.items(), key=lambda x: (-x[1],x[0])))
language_sub = dict(sorted(language_sub.items(), key=lambda x: (-x[1],x[0])))


print(f"Results:")
[print(f"{name} | {points}") for name, points in people_res.items()]

print(f"Submissions:")
[print(f"{lan} - {sub}") for lan, sub in language_sub.items()]