import re

pattern = r'(\*|@)([A-Z][a-z]{2,})\1: \[([A-Za-z])\]\|\[([A-Za-z]+)\]\|\[([A-Za-z]+)\]\|$'

n = int(input())

for i in range(n):
    message = input()

    match = re.findall(pattern, message)

    if not match:
        print("Valid message not found!")
        continue

    print(f"{match[0][1]}: {ord(match[0][2])} {ord(match[0][3])} {ord(match[0][4])}")
