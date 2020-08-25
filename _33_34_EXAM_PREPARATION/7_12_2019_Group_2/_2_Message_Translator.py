import re

pattern = r'^(!)([A-Z][a-z]{3,})\1:\[([A-Za-z]{8,})\]$'

n = int(input())

for i in range(n):
    text = input()
    match = re.fullmatch(pattern, text)

    if match is None:
        print("The message is invalid")
    else:
        string = match[2] + ":"
        for char in match[3]:
            string += " " + str(ord(char))
        print(f"{string}")
