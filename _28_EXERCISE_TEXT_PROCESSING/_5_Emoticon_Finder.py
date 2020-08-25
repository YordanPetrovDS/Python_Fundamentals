text = input()

for index, letter in enumerate(text):
    if letter == ":":
        print(f"{text[index] + text[index + 1]}")
