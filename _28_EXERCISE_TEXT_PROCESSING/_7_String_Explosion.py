line = input()
total_strength = 0
index = 0
while index < len(line):
    char = line[index]

    if char == ">":
        strength = int(line[index + 1])
        total_strength += strength
    else:
        if total_strength > 0:
            line = line[:index] + line[index + 1:]
            total_strength -= 1
            index -= 1

    index += 1

print(line)
