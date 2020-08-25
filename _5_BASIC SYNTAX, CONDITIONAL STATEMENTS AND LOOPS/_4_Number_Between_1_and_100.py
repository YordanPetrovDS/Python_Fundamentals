number = float(input())
# while number not in (range(1, 101)):
#     number = float(input())
# else:
#     print(number)

while number < 1 or number > 100:
    number = float(input())

print(f'The number {number:.0f} is between 1 and 100')
