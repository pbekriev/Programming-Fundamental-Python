def create_heroes(heroes_dict, number_of_heroes):
    for _ in range(number_of_heroes):
        list = input().split()
        hero_name, hit_points, mana_points = list[0], int(list[1]), int(list[2])
        heroes_dict[hero_name] = [hit_points, mana_points]
    return heroes_dict


def playin_game(heroes_dict):
    command = input()
    while command != "End":
        split_command = command.split(" - ")
        current_command = split_command[0]

        if current_command == "CastSpell":
            hero_name, mp_needed, spell_name = split_command[1], int(split_command[2]), split_command[3]
            availabel_mp = heroes_dict[hero_name][1]

            if availabel_mp >= mp_needed:
                heroes_dict[hero_name][1] -= mp_needed
                current_mp = heroes_dict[hero_name][1]
                print(f"{hero_name} has successfully cast {spell_name} and now has {current_mp} MP!")
            else:
                print(f"{hero_name} does not have enough MP to cast {spell_name}!")

        elif current_command == "TakeDamage":
            hero_name, damage, attacker = split_command[1], int(split_command[2]), split_command[3]
            availabel_hp = heroes_dict[hero_name][0]

            if availabel_hp - damage > 0:
                heroes_dict[hero_name][0] -= damage
                current_hp = heroes_dict[hero_name][0]
                print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {current_hp} HP left!")
            else:
                del heroes_dict[hero_name]
                print(f"{hero_name} has been killed by {attacker}!")

        elif current_command == "Recharge":
            hero_name, amount = split_command[1], int(split_command[2])
            availabel_mp = heroes_dict[hero_name][1]
            if availabel_mp + amount > 200:
                amount = 200 - availabel_mp
                heroes_dict[hero_name][1] += amount
            else:
                heroes_dict[hero_name][1] += amount
            print(f"{hero_name} recharged for {amount} MP!")
        elif current_command == "Heal":
            hero_name, amount = split_command[1], int(split_command[2])
            availabel_hp = heroes_dict[hero_name][0]
            if availabel_hp + amount > 100:
                amount = 100 - availabel_hp
                heroes_dict[hero_name][0] += amount
            else:
                heroes_dict[hero_name][0] += amount
            print(f"{hero_name} healed for {amount} HP!")

        command = input()

    return heroes_dict


def print_func(heroes_dict):
    print_result = ""

    for hero in heroes_dict:
        print_result += f"{hero}\n  HP: {heroes_dict[hero][0]}\n  MP: {heroes_dict[hero][1]}\n"

    return print_result

def heroes_of_code(number_of_heroes):
    heroes_dict = {}

    create_heroes(heroes_dict, number_of_heroes)

    playin_game(heroes_dict)

    print(print_func(heroes_dict))


number_of_heroes = int(input())
heroes_of_code(number_of_heroes)
