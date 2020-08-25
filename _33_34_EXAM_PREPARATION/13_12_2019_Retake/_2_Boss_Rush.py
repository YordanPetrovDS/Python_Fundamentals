import re

pattern = r'^(\|)([A-Z]{4,})\1:(#)([A-Za-z]+ [A-Za-z]+)\3$'

n = int(input())

for i in range(n):
    boss = input()

    match = re.fullmatch(pattern, boss)

    if match is None:
        print("Access denied!")
    else:
        print(f"{match[2]}, The {match[4]}")
        print(f">> Strength: {len(match[2])}")
        print(f">> Armour: {len(match[4])}")
