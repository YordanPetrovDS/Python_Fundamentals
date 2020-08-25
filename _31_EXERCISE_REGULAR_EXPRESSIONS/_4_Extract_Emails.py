import re

text = input()

# user_pattern = fr'(^|(?<=\s))[a-z0-9]+([\.\-_][a-z0-9]+)*'
# host_pattern = fr'[a-z]+([\.\-][a-z]+)?(\.[a-z]+)(\.[a-z]+)?'
# pattern = fr'{user_pattern}@{host_pattern}'
# users = re.finditer(pattern, text, re.MULTILINE | re.IGNORECASE)
#
# for match in users:
#     print(match[0])
user_pattern = r'( |^)[a-zA-Z0-9]+((\.|\-|_)[a-zA-Z0-9]+)*'
host_pattern = r'[a-zA-Z]+(-[a-zA-Z]+)*(\.[a-zA-Z]+(-[a-zA-Z]+)*)+'
pattern = rf'{user_pattern}@{host_pattern}'

emails = re.finditer(pattern, text)

for email in emails:
    print(email[0])
