import re

text = input()
while True:
    if not text:
        break

    pattern = r'w{3}\.([a-zA-Z0-9]+(-[a-zA-Z0-9]+)*)(\.[a-z]+)+'
    users = re.finditer(pattern, text, re.MULTILINE)

    for match in users:
        print(match.group())
    text = input()