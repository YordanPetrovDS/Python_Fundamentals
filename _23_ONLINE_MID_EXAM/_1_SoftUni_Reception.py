employee1 = int(input())
employee2 = int(input())
employee3 = int(input())
total_sum_employee = employee1 + employee2 + employee3
students = int(input())
hour_counter = 0

while students > 0:
    hour_counter += 1
    if hour_counter % 4 == 0:
        continue
    else:
        students -= total_sum_employee

print(f"Time needed: {hour_counter}h.")
