def add_func(animals_info, areas_info, animal_name, needed_food_quantity, area):
    if animal_name not in animals_info:
        animals_info[animal_name] = 0
    animals_info[animal_name] += needed_food_quantity
    if area not in areas_info:
        areas_info[area] = [animal_name]
    if animal_name not in areas_info[area]:
        areas_info[area].append(animal_name)
    return animals_info, areas_info


def feed_func(animals_info, areas_info, animal_name, food):
    if animal_name in animals_info:
        animals_info[animal_name] -= food
    if animals_info[animal_name] <= 0:
        del animals_info[animal_name]
        print(f"{animal_name} was successfully fed")
        for key, val in areas_info.items():
            if animal_name in val:
                areas_info[key].remove(animal_name)
    return animals_info, areas_info


def print_func(animals_info, areas_info):
    print_result = ""
    if animals_info:
        print_result += "Animals:"
        for animal, food in animals_info.items():
            print_result += f"\n {animal} -> {food}g"
    if areas_info:
        print_result += f"\nAreas with hungry animals:"
        for area, animals in areas_info.items():
            if animals:
                print_result += f"\n {area}: {len(animals)}"
    print(print_result)

animals_info = {}
areas_info = {}
command = input()
while command != "EndDay":
    split_command = command.split(": ")
    current_command = split_command[0]
    information = split_command[1]
    if current_command == "Add":
        current_command_split = information.split("-")
        animal_name, needed_food_quantity, area = current_command_split[0], int(current_command_split[1]), \
                                                  current_command_split[2]
        add_func(animals_info, areas_info, animal_name, needed_food_quantity, area)

    elif current_command == "Feed":
        current_command_split = information.split("-")
        animal_name, food = current_command_split[0], int(current_command_split[1])
        feed_func(animals_info, areas_info, animal_name, food)

    command = input()

print_func(animals_info, areas_info)
