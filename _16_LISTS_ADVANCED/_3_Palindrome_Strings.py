def is_palindrome(word):
    # return word == "".join(reversed(word))
    return word == word[::-1]


words = input().split()
search_word = input()

palindrome_words = [word for word in words if is_palindrome(word)]

print(palindrome_words)

print(f"Found palindrome {palindrome_words.count(search_word)} times")