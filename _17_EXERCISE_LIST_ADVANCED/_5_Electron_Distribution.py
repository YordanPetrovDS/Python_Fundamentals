num = int(input())

list_atoms = []
n = 1
while num > 0:
    current_atoms = 2 * n ** 2
    if current_atoms > num:
        current_atoms = num

    list_atoms.append(current_atoms)
    num -= current_atoms
    n += 1
print(list_atoms)
