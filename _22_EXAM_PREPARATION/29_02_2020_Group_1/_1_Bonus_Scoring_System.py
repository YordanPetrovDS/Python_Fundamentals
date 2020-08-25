import math

students_count = int(input())
lectures_count = int(input())
initial_bonus = int(input())

total_bonus = 0

for _ in range(students_count):
    student_attendances = int(input())
    current_tot_bonus = (student_attendances / lectures_count) * (5 + initial_bonus)
    if current_tot_bonus > total_bonus:
        total_bonus = current_tot_bonus
        attendance_count = student_attendances

if total_bonus > 0:
    print(f"Max Bonus: {math.ceil(total_bonus)}.")
    print(f"The student has attended {attendance_count} lectures.")
else:
    print(f"Max Bonus: {total_bonus}.")
    print(f"The student has attended {total_bonus} lectures.")
