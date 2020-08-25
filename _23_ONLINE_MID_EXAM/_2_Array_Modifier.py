numbers = list(map(int, input().split()))
command = input()

while command != "end":
    arg = command.split()

    if arg[0] == "swap":
        index1 = int(arg[1])
        index2 = int(arg[2])
        numbers[index1], numbers[index2] = numbers[index2], numbers[index1]
    elif arg[0] == "multiply":
        index1 = int(arg[1])
        index2 = int(arg[2])
        numbers[index1] = numbers[index1] * numbers[index2]
    elif arg[0] == "decrease":
        for index in range(len(numbers)):
            numbers[index] -= 1

    command = input()

print(f"{', '.join(map(str, numbers))}")
