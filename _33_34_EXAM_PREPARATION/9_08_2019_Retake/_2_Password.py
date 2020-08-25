import re

pattern = r'^(.+)>(\d{3})\|([a-z]{3})\|([A-Z]{3})\|([^<>]{3})<(\1)$'

n = int(input())

for i in range(n):
    password = input()

    match = re.fullmatch(pattern, password)

    if match is None:
        print("Try another password!")
    else:
        print(f"Password: {match[2]}{match[3]}{match[4]}{match[5]}")
