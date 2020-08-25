string = input()
string_new = ""
start_index = 0
for index in range(len(string)):
    if string[index].isnumeric():
        if index < (len(string) - 1) and string[index + 1].isnumeric():
            string_new += string[start_index:index] * (int(string[index] + string[index + 1]))
            start_index = index + 2
        else:
            string_new += string[start_index:index] * int(string[index])
            start_index = index + 1

string_new = string_new.upper()

print(f"Unique symbols used: {len(set(string_new))}")
print(string_new)

