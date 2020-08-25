numbers = list(map(int, input().split()))
total_sum = 0
for num in numbers:
    total_sum += num
avg = total_sum / len(numbers)

number_greater = [num for num in numbers if num > avg]
number_greater.sort(reverse=True)

top_5_numbers = [num for index, num in enumerate(number_greater) if index < 5]

if not top_5_numbers:
    print("No")
else:
    print(f"{' '.join(map(str, top_5_numbers))}")
