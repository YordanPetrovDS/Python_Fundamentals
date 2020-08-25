import re

text = input()
# \2  - back-reference to second group ("([/\.-])" - if contains separator "/" or "." or "-")
pattern = r'(\d{2})([/\.-])([A-z][a-z]{2})\2(\d{4})'


for match in re.findall(pattern, text):
    day, _, month, year = match
    print(f"Day: {day}, Month: {month}, Year: {year}")
