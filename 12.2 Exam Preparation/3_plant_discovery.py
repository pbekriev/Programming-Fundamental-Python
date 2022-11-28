def add_plants(numbers_of_plants, plants_dict):
    for _ in range(numbers_of_plants):
        plants_info = input().split("<->")
        plants_dict[plants_info[0]] = [plants_info[1]]
    return plants_dict


def exhibition(plants_dict):
    command = input()
    while command != "Exhibition":
        split_command = command.split(": ")
        current_command = split_command[0]
        if current_command == "Rate":
            plant, rating = split_command[1].split(" - ")
            if plant not in plants_dict:
                print("error")
            else:
                plants_dict[plant].append(int(rating))

        elif current_command == "Update":
            plant, new_rarity = split_command[1].split(" - ")
            if plant not in plants_dict:
                print("error")
            else:
                plants_dict[plant][0] = int(new_rarity)

        elif current_command == "Reset":
            plant = split_command[1]
            if plant not in plants_dict:
                print("error")
            else:
                old = plants_dict[plant][0]
                plants_dict[plant] = [old]

        command = input()


def print_func(plants_dict):
    print_result = ""
    print("Plants for the exhibition:")
    for plant in plants_dict:
        if len(plants_dict[plant]) > 1:
            rates = plants_dict[plant][1:]
            avr_rates = sum(rates) / len(rates)
            print_result += f"- {plant}; Rarity: {plants_dict[plant][0]}; Rating: {avr_rates:.2f}\n"
        else:
            print_result += f"- {plant}; Rarity: {plants_dict[plant][0]}; Rating: 0.00\n"
    print(print_result)


def main_func(numbers_of_plants):
    plants_dict = {}
    add_plants(numbers_of_plants, plants_dict)
    exhibition(plants_dict)
    print_func(plants_dict)


numbers_of_plants = int(input())
main_func(numbers_of_plants)
