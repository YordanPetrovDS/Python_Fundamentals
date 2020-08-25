import re

pattern = r'^(\$|\%)([A-Z][a-z]{3,})\1: \[([0-9]+)\]\|\[([0-9]+)\]\|\[([0-9]+)\]\|$'

n = int(input())

for i in range(n):
    text = input()

    match = re.findall(pattern, text)
    if not match:
        print("Valid message not found!")
        continue

    print(f"{match[0][1]}: {chr(int(match[0][2]))}{chr(int(match[0][3]))}{chr(int(match[0][4]))}")
