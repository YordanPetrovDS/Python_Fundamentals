import re

pattern = r'^(U\$)([A-Z][a-z]{2,})\1(P@\$)([A-Za-z]{5,}[0-9]+)\3$'
n = int(input())

counter = 0
for i in range(n):
    registration = input()
    match = re.fullmatch(pattern, registration)

    if match is None:
        print("Invalid username or password")
    else:
        counter += 1
        print("Registration was successful")
        print(f"Username: {match[2]}, Password: {match[4]}")

print(f"Successful registrations: {counter}")
