def int_to_char(word):
    arr = list(word)
    num_str = ""

    while True:
        if not arr[0].isdigit():
            break

        num_str += arr[0]
        arr.pop(0)

    num = int(num_str)
    arr.insert(0, chr(num))
    return "".join(arr)


def switch_letters(word):
    list_chars = list(word)
    list_chars[1], list_chars[-1] = list_chars[-1], list_chars[1]
    return "".join(list_chars)


def decrypt_word(word):
    word = int_to_char(word)
    word = switch_letters(word)
    return word


words = input().split()

words = [decrypt_word(word) for word in words]

print(" ".join(words))
