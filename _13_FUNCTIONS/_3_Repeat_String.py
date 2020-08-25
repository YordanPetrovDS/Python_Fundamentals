string_input = input()
num = int(input())


# def string(str, n):
#     new_string = ""
#     for i in range(0, n):
#         new_string += str
#     return new_string


# def string(str, n):
#     return str*n

# Recursion
def string(str, n):
    if n < 1:
        return ""
    return str + string(str, n=n - 1)


print(string(string_input, num))
