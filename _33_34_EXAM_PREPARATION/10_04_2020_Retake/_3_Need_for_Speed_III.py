car_count = int(input())
car_dict = {}

for _ in range(car_count):
    car_specs = input().split("|")
    car_dict[car_specs[0]] = [int(car_specs[1]), int(car_specs[2])]
    # car_dict[car_specs[0]] = {}
    # car_dict[car_specs[0]]["mileage"] = int(car_specs[1])
    # car_dict[car_specs[0]]["fuel"] = int(car_specs[2])

input_command = input()

while input_command != "Stop":
    tokens = input_command.split(" : ")
    car = tokens[1]
    command = tokens[0]
    if command == "Drive":
        distance = int(tokens[2])
        fuel = int(tokens[3])
        # if car_dict[car]["fuel"] < fuel:
        if car_dict[car][1] < fuel:
            print("Not enough fuel to make that ride")
        else:
            # car_dict[car]["fuel"] -= fuel
            # car_dict[car]["mileage"] += distance
            car_dict[car][1] -= fuel
            car_dict[car][0] += distance
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
            # if car_dict[car]["mileage"] > 100000:
            if car_dict[car][0] > 100000:
                car_dict.pop(car)
                print(f"Time to sell the {car}!")
    elif command == "Refuel":
        fuel = int(tokens[2])
        current_fuel = car_dict[car][1]
        if (current_fuel + fuel) > 75:
            fuel_gained = 75 - current_fuel
            car_dict[car][1] = 75
        else:
            fuel_gained = fuel
            car_dict[car][1] += fuel
        print(f"{car} refueled with {fuel_gained} liters")
    elif command == "Revert":
        kilometers = int(tokens[2])

        if (car_dict[car][0] - kilometers) < 10000:
            car_dict[car][0] = 10000
        else:
            car_dict[car][0] = car_dict[car][0] - kilometers
            print(f"{car} mileage decreased by {kilometers} kilometers")

    input_command = input()

# car_dict = dict(sorted(car_dict.items(), key=lambda x: (-x[1]["mileage"], x[0])))
car_dict = dict(sorted(car_dict.items(), key=lambda x: (-x[1][0], x[0])))

# [print(f"{car} -> Mileage: {"mileage"} kms, Fuel in the tank: {spec["fuel"]} lt.") for car, spec in car_dict.items()]
[print(f"{car} -> Mileage: {spec[0]} kms, Fuel in the tank: {spec[1]} lt.") for car, spec in car_dict.items()]
