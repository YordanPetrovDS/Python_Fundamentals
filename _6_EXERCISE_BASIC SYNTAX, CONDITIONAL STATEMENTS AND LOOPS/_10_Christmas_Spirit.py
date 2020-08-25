quantity = int(input())
days = int(input())
budget = 0
totalSpirit = 0

for i in range(1, days + 1):
    if i % 11 == 0:
        quantity += 2
    if i % 2 == 0:
        budget += quantity * 2
        totalSpirit += 5
    if i % 3 == 0:
        budget += quantity * 8
        totalSpirit += 13
    if i % 5 == 0:
        budget += quantity * 15
        totalSpirit += 17
        if i % 3 == 0:
            totalSpirit += 30
    if i % 10 == 0:
        totalSpirit -= 20
        budget += 23

if days % 10 == 0:
    totalSpirit -= 30

print(f"Total cost: {budget}")
print(f"Total spirit: {totalSpirit}")
