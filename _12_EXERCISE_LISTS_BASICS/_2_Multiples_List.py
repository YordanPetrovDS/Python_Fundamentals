factor = int(input())
count = int(input())

num_list = []
for num in range(1, count + 1):
    num_list.append(factor * num)

print(num_list)
