# input_version = list(map(int, input().split(".")))
#
# input_version[2] += 1
#
# if input_version[2] == 10:
#     input_version[2] = 0
#     input_version[1] += 1
#
# if input_version[1] == 10:
#     input_version[1] = 0
#     input_version[0] += 1
#
# print(".".join(map(str, input_version)))

num = int(input().replace(".", ""))
new_version = num + 1

print(".".join(list(str(new_version))))
