import re

pattern = r'^(@#+)([A-Z][A-Za-z0-9]{4,}[A-Z])(@#+)$'
n = int(input())

for i in range(n):
    text = input()
    match = re.fullmatch(pattern, text)

    if match is None:
        print("Invalid barcode")
        continue

    string = ""
    for char in match[2]:
        if char.isdigit():
            string += char

    if string == "":
        string = "00"
    print(f"Product group: {string}")
