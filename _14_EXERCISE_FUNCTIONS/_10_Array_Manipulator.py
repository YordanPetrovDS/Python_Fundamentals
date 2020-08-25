def exchange(array, index):
    current_list1 = []
    current_list2 = []
    current_list = []

    if int(index) < 0 or int(index) > (len(array) - 1):
        print("Invalid index")
        return array
    elif int(index) < (len(array) - 1):
        current_list1 = array[int(index) + 1:]
        current_list2 = array[:int(index) + 1]
        current_list = current_list1 + current_list2
        return current_list
    elif int(index) == (len(array) - 1):
        current_list = array
        return current_list


def max_min_even_odd(array, number_type, type_):
    list_elements = []
    max_number = 0
    min_number = 1001
    is_valid = False
    for index, ele in enumerate(array, 0):
        if number_type == 'even':
            if type_ == "max":
                if int(ele) % 2 == 0 and max_number <= int(ele):
                    max_number = int(ele)
                    list_elements.append(int(index))
                    is_valid = True
            elif type_ == "min":
                if int(ele) % 2 == 0 and min_number >= int(ele):
                    min_number = int(ele)
                    list_elements.append(int(index))
                    is_valid = True
        elif number_type == 'odd':
            if type_ == "max":
                if int(ele) % 2 != 0 and max_number <= int(ele):
                    max_number = int(ele)
                    list_elements.append(int(index))
                    is_valid = True
            elif type_ == "min":
                if int(ele) % 2 != 0 and min_number >= int(ele):
                    min_number = int(ele)
                    list_elements.append(int(index))
                    is_valid = True

    if not is_valid:
        return print('No matches')
    elif type_ == "max":
        max_ = max(list_elements)
        return print(max_)
    elif type_ == "min":
        min_ = max(list_elements)
        return print(min_)


def first_last_even_odd(array, type_, count, num_type):
    element_list = []
    len_arr = len(array)
    if int(count) > len(array):
        return print('Invalid count')

    for ele in array:
        if num_type == 'even':
            if type_ == "first":
                if int(ele) % 2 == 0 and len(element_list) <= int(count) - 1:
                    element_list.append(int(ele))
            elif type_ == "last":
                if int(ele) % 2 == 0:
                    element_list.append(int(ele))
        elif num_type == 'odd':
            if type_ == "first":
                if int(ele) % 2 != 0 and len(element_list) <= int(count) - 1:
                    element_list.append(int(ele))
            elif type_ == "last":
                if int(ele) % 2 != 0:
                    element_list.append(int(ele))

    if type_ == 'last' and len(element_list) >= int(count):
        last_list = element_list[len(element_list) - int(count):]
        return print(last_list)
    else:
        return print(element_list)


input_array = input().split()
command = input()
current_list = []
while command != 'end':
    current_command = command.split()
    if current_command[0] == 'exchange':
        current_list = exchange(input_array, current_command[1])
        input_array = current_list
    elif current_command[0] in ['max', 'min']:
        max_min_even_odd(input_array, current_command[1], current_command[0])
    elif current_command[0] in ['first', 'last']:
        first_last_even_odd(input_array, current_command[0], current_command[1], current_command[2])

    command = input()

final_list = [int(i) for i in current_list]
print(final_list)
