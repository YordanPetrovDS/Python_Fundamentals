def sum_numbers(a, b):
    return a + b


def subtract(first_number, second_number):
    return first_number - second_number


def add_and_subtract(num_one, num_two, num_three):
    print(subtract(sum_numbers(num_one, num_two), num_three))


add_and_subtract(int(input()), int(input()), int(input()))
