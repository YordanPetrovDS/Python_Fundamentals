fires = input().split("#")
water = int(input())
current_fire = ""
effort = 0
total_fire = 0
fires_list = []

for fire in fires:
    current_fire = fire.split(" = ")
    valid = False

    if water < int(current_fire[1]):
        continue

    if current_fire[0] == "High" and (81 <= int(current_fire[1]) <= 125):
        valid = True
    elif current_fire[0] == "Medium" and (51 <= int(current_fire[1]) <= 80):
        valid = True
    elif current_fire[0] == "Low" and (1 <= int(current_fire[1]) <= 50):
        valid = True

    if valid:
        water -= int(current_fire[1])
        effort += 0.25 * int(current_fire[1])
        total_fire += int(current_fire[1])
        fires_list.append(" - " + current_fire[1])

print("Cells:")
[print(fire) for fire in fires_list]
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")
