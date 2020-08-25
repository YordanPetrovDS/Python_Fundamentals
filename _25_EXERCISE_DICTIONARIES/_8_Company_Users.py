command = input()
company_dict = {}

while command != "End":
    args = command.split(" -> ")

    if args[0] in company_dict:
        if args[1] not in company_dict[args[0]]:
            company_dict[args[0]].append(args[1])
    else:
        company_dict[args[0]] = [args[1]]

    command = input()

company_dict = dict(sorted(company_dict.items(), key=lambda el: el[0]))

for key in company_dict.keys():
    print(f"{key}")
    for item in company_dict[key]:
        print(f"-- {item}")
