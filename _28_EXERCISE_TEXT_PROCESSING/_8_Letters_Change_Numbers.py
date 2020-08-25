def get_letter_position_in_alphabet(letter):
    # ascii tables
    position = ord(letter) - 64

    if letter.islower():
        position = ord(letter) - 96

    return position


def calculate_item_result(item):
    first_letter = item[0]
    last_letter = item[-1]
    number = int(item[1:-1])
    first_letter_position = get_letter_position_in_alphabet(first_letter)
    last_letter_position = get_letter_position_in_alphabet(last_letter)
    result = 0

    if first_letter.isupper():
        result = number / first_letter_position
    else:
        result = number * first_letter_position

    if last_letter.isupper():
        result -= last_letter_position
    else:
        result += last_letter_position

    return result


items = input().split()
result = 0
for item in items:
    result += calculate_item_result(item)

print(f"{result:.2f}")
