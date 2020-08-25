import re

# pattern = r"\b_(?P<variable>[A-Za-z0-9]+)\b"
# matches = re.findall(pattern, text)

text = input()
pattern = r"\b_([A-Za-z0-9]+)\b"

matches = re.finditer(pattern, text)

all_var_names = []

for match in matches:
    all_var_names.append(match[1])

print(",".join(all_var_names))
