def chars_as_string(start, end):
    res = ""
    for i in range(ord(start) + 1, ord(end)):
        res += chr(i) + " "
        # print(chr(i), end=" ")
    return res


# lstrip(res)

start = input()
end = input()
print(chars_as_string(start, end))
