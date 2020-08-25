word = input()
reversed_word = ""

# Ctrl+/ - Commenting scrips
# Ctrl+Shift+/ - Uncommenting
# for i in range(len(word) - 1, -1, -1):
#     reversed_word += word[i]
# print(reversed_word)

i = len(word)
reversed_word = ""

while i > 0:
    i -= 1
    reversed_word += word[i]
print(reversed_word)
