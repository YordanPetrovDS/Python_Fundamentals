# def word_by_length(word):
#     return word * len(word)


# words = input().split()
# print("".join(map(word_by_length, words)))
# print("".join(map(lambda word: word * len(word), words)))
print("".join(map(lambda word: word * len(word), input().split())))
