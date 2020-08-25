books_list = input().split("&")
action = input()

while action != "Done":
    action_split = action.split(" | ")
    command = action_split[0]
    book = action_split[1]
    if command == "Add Book":
        if book not in books_list:
            books_list.insert(0, book)
    elif command == "Take Book":
        if book in books_list:
            books_list.remove(book)
    elif command == "Swap Books":
        book1 = book
        book2 = action_split[2]
        if book1 and book2 in books_list:
            book1_index = books_list.index(book1)
            book2_index = books_list.index(book2)
            books_list[book1_index], books_list[book2_index] = books_list[book2_index], books_list[book1_index]
    elif command == "Insert Book":
        books_list.append(book)
    elif command == "Check Book":
        index = int(book)
        if 0 <= index < len(books_list):
            print(f"{books_list[index]}")

    action = input()

print(f"{', '.join(books_list)}")
