command = input()
course_name = {}

while command != "end":
    args = command.split(" : ")

    if args[0] not in course_name:
        course_name[args[0]] = [args[1]]
    else:
        course_name[args[0]].append(args[1])

    command = input()

course_name = dict(sorted(course_name.items(), key=lambda el: -len(el[1])))

for i in course_name.keys():
    course_name[i].sort()

for key in course_name.keys():
    print(f"{key}: {len(course_name[key])}")
    for item in course_name[key]:
        print(f"-- {item}")
