n = int(input())
litres_sum = 0

for i in range(1, n + 1):
    litres = int(input())
    litres_sum += litres
    if litres_sum > 255:
        litres_sum -= litres
        print("Insufficient capacity!")

print(f"{litres_sum}")
