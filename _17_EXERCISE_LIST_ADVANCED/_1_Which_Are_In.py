words = input().split(", ")
input_string = input()
list_new = [i for i in words if i in input_string]
print(list_new)
