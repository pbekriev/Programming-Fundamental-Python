def add_cars(number_of_cars, cars):
    for _ in range(number_of_cars):
        data = input().split("|")
        cars[data[0]] = [int(data[1]), int(data[2])]
    return cars


def print_func(cars):
    print_result = ""
    for car in cars:
        print_result += f"{car} -> Mileage: {cars[car][0]} kms, Fuel in the tank: {cars[car][1]} lt.\n"
    print(print_result)


def drive_func(split_command, cars):
    car, distance, fuel = split_command[1], int(split_command[2]), int(split_command[3])

    if cars[car][1] < fuel:
        print("Not enough fuel to make that ride")
    else:
        cars[car][0] += distance
        cars[car][1] -= fuel
        print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
    if cars[car][0] >= 100000:
        del cars[car]
        print(f"Time to sell the {car}!")


def refuel_func(split_command, cars):
    car, fuel = split_command[1], int(split_command[2])

    if cars[car][1] + fuel > 75:
        fuel = 75 - cars[car][1]
        cars[car][1] = 75
    else:
        cars[car][1] += fuel

    print(f"{car} refueled with {fuel} liters")


def revert_func(split_command, cars):
    car, kilometers = split_command[1], int(split_command[2])

    if cars[car][0] - kilometers < 10000:
        cars[car][0] = 10000
    else:
        cars[car][0] -= kilometers
        print(f"{car} mileage decreased by {kilometers} kilometers")


def the_game(cars):
    command = input()
    while command != "Stop":
        split_command = command.split(" : ")
        current_command = split_command[0]

        if current_command == "Drive":
            drive_func(split_command, cars)

        elif current_command == "Refuel":
            refuel_func(split_command, cars)

        elif current_command == "Revert":
            revert_func(split_command, cars)

        command = input()

    print_func(cars)


def main_program(number_of_cars):
    cars = {}

    add_cars(number_of_cars, cars)

    the_game(cars)


number_of_cars = int(input())
main_program(number_of_cars)
