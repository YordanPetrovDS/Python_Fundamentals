import re

text = input()

pattern = r'(@|#)(?P<first>[a-zA-Z]{3,})\1\1(?P<second>[A-Za-z]{3,})\1'
matches = re.finditer(pattern, text)
# pattern = r'(@|#)([a-zA-Z]{3,})\1\1([A-Za-z]{3,})\1'
# matches = re.findall(pattern, text)
# first = match[1]
# second = match[2]
founded_matches = []
counter = 0

for match in matches:
    counter += 1

    first = match.group('first')
    second = match.group('second')
    if first == second[::-1]:
        pair = first + ' <=> ' + second
        founded_matches.append(pair)

if counter == 0:
    print(f'No word pairs found!')
else:
    print(f'{counter} word pairs found!')

if founded_matches:
    print('The mirror words are:')
    print(', '.join(founded_matches))
else:
    print('No mirror words!')