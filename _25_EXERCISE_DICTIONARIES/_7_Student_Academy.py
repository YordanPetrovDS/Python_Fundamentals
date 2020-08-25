students = int(input())
students_dict = {}
top_students = {}
for _ in range(students):
    name = input()
    grade = float(input())

    if name in students_dict:
        students_dict[name].append(grade)
    else:
        students_dict[name] = [grade]

# for key, item in students_dict.items():
#     if sum(item) / len(item) >= 4.50:
#         top_students[key] = sum(item) / len(item)
top_students = {k: sum(v) / len(v) for k, v in students_dict.items() if sum(v) / len(v) >= 4.50}

top_students = dict(sorted(top_students.items(), key=lambda el: -el[1]))

[print(f"{name} -> {grade:.2f}") for name, grade in top_students.items()]
