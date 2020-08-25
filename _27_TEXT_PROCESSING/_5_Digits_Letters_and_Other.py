def all_digits(text):
    return get_all_characters_matching_condition(
        text,
        lambda char: char.isdigit()
    )

    # digits = ""
    # for char in text:
    #     if char.isdigit():
    #         digits += char
    # return digits


def all_letters(text):
    return get_all_characters_matching_condition(
        text,
        lambda char: char.isalpha()
    )
    # letters = ""
    # for char in text:
    #     if char.isalpha():
    #         letters += char
    # return letters


def all_other_characters(text):
    return get_all_characters_matching_condition(
        text,
        lambda char: not char.isalnum()
    )
    # other_characters = ""
    # for char in text:
    #     if not char.isdigit() and not char.isalpha():
    #         other_characters += char
    # return other_characters


def get_all_characters_matching_condition(text, condition_fn):
    result = ""
    for char in text:
        if condition_fn(char):
            result += char
    return result


text = input()

print(all_digits(text))
print(all_letters(text))
print(all_other_characters(text))
