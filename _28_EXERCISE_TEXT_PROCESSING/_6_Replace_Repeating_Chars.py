line = input()

# for index, char in enumerate(line):
#     if index == 0 or char != line[index - 1]:
#         print(char, end="")

[print(char, end="") for index, char in enumerate(line) if index == 0 or char != line[index - 1]]
