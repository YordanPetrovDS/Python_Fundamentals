def reverse(string):
    return string[::-1]
    # return ' '.join(reverse(string))
    # s = ""
    # for char in reversed(string):
    #     s += char
    # return s


words = []

while True:
    command = input()
    if command == "end":
        break
    words.append(command)

# for word in words:
#     print(f"{word} = {reverse(word)}")

[print(f"{word} = {reverse(word)}") for word in words]
