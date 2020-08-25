def factorial_calculation(number):
    factorial = 1
    for i in range(1, number + 1):
        factorial *= i
    return factorial


num1 = int(input())
num2 = int(input())

print(f"{(factorial_calculation(num1) / factorial_calculation(num2)):.2f}")
