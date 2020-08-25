words = list(map(str, input().split(", ")))

for word in words:
    if 3 <= len(word) <= 16:
        if word.isalnum() or ("_" in word) or ("-" in word):
            print(f"{word}")
