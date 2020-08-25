# from _collections import defaultdict

text = input()
# my_dict = defaultdict(int)
my_dict = {}
for ch in text:
    if ch == " ":
        continue
    if ch in my_dict:
        my_dict[ch] += 1
    else:
        my_dict[ch] = 1

[print(f"{letter} -> {quantity}") for letter, quantity in my_dict.items()]


