n = int(input())
sum_ = 0
for i in range(1, n + 1):
    character = input()
    sum_ += ord(character)
print(f"The sum equals: {sum_}")
