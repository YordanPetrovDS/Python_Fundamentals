import re

pattern = r'(\:\:|\*\*)([A-Z][a-z]{2,})\1'

text = input()
cool_threshold = 1
for char in text:
    if char.isdigit():
        cool_threshold *= int(char)

matches = re.finditer(pattern, text)

emojis_count = 0
cool_emojies = []
for match in matches:
    emojis_count += 1

    current_coolness = 0
    for char in match.group(2):
        current_coolness += ord(char)

    if current_coolness < cool_threshold:
        continue

    cool_emojies.append(match.group(1) + match.group(2) + match.group(1))

print(f"Cool threshold: {cool_threshold}")
print(f"{emojis_count} emojis found in the text. The cool ones are:")
[print(f"{emoji}") for emoji in cool_emojies]
