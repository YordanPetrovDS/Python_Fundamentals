operator = input()
first_number = int(input())
second_number = int(input())


def solve(action, a, b):
    if action == "multiply":
        return a * b
    elif action == "divide":
        return a // b
    elif action == "add":
        return a + b
    elif action == "subtract":
        return a - b


print(solve(operator, first_number, second_number))
